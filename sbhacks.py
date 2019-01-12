from flask import Flask, render_template
import pyrebase

app = Flask(__name__)


config = {
  "apiKey": "AIzaSyDLZ672i6TUb9FwpIasc0MzfDhFOMrOYHI",
  "authDomain": "sb-hacks-bf124.firebaseapp.com",
  "databaseURL": "https://sb-hacks-bf124.firebaseio.com",
  "projectId": "sb-hacks-bf124",
  "storageBucket": "sb-hacks-bf124.appspot.com",
  "messagingSenderId": "544177410232"
};

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def about():
    return render_template('login.html')

@app.route("/createAccount")
def create_account():
    return render_template('createAccount.html')

@app.route("/dashboard")
def dashboard():
    card = {"ベトナム人" : "Vietnamese"}
    db.child("word").push(card)
    return render_template('dashboard.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0')
