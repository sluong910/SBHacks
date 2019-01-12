from flask import Flask, render_template, request
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
auth = firebase.auth()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    # if request.method == 'POST':
    #     email = request.form['email']
    #     password = request.form['password']
    #     user = auth.sign_in_with_email_and_password(email, password)
    return render_template('login.html')
    

@app.route("/createAccount", methods=['GET', 'POST'])
def create_account():
    msg = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        auth.create_user_with_email_and_password(email, password)
        msg = 'Account Successfully Created'
    return render_template('createAccount.html', message=msg)

@app.route("/dashboard", methods=['POST'])
def dashboard():
    # card = {"ベトナム人" : "Vietnamese"}
    # db.child("word").push(card)

    return render_template('dashboard.html')


@app.route("/settings")
def settings():
    return render_template('settings.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0')
