from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def about():
    return render_template('login.html')

@app.route("/createAccount")
def create_account():
    return render_template('createAccount.html')


if __name__ == '__main__':
    app.run(debug=True)