from flask import Flask, render_template, request
import pyrebase
# import ocv_test
import ocv_test_actual_final
import re
import urllib
from trans_lang import LANGUAGES
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

user = ''

@app.route("/", methods=['GET', 'POST'])
def index():
    global user
    user = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            return render_template('dashboard.html')
        except:
            return render_template('login.html')
    return render_template('login.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route("/createAccount", methods=['GET', 'POST'])
def create_account():
    msg = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            auth.create_user_with_email_and_password(email, password)
            msg = 'Account Successfully Created'
        except:
            return render_template('createAccount.html', message="Error Creating Account")
    return render_template('createAccount.html', message=msg)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    # user_info = current_email
    global user

    if user == '':
        return render_template('login.html')
    try:
        if request.method == 'POST':
            s = request.form['select-language']
            localId = auth.get_account_info(user['idToken'])['users'][0]['localId']

            filestr = request.files['file'].read()

            outp = ocv_test_actual_final.main(filestr,LANGUAGES[s][0],LANGUAGES[s][1],0)
            # print(outp)
            # outp = ocv_test.parse_img(filestr)
            text1 = re.sub(r'\s+', ' ', outp[0])
            text2 = re.sub(r'\s+', ' ', outp[1])
            d = outp[2]

            d2 = dict()

            for k in d.keys():
                if not (re.sub(r'\s+', ' ', k) == ' ' or re.sub(r'\s+', ' ', d[k]) == ' '):
                    d2[re.sub(r'\s+', ' ', k)] = re.sub(r'\s+', ' ', d[k])

            # print(text1, text2)
            # card = {text1:text2}
            # db.child("word").push(card)
            if d2:
                for e in d2.keys():
                    db.child(localId).child(text1).child(text2).child(e).set(d2[e].lower())
            else:
                db.child(localId).child(text1).set(text2)
        return render_template('dashboard.html')
    except:
        return render_template('login.html')


@app.route("/AboutUs")
def settings():
    return render_template('AboutUs.html')

@app.route("/flash")
def flashcards():
<<<<<<< HEAD
    lt = []
    try:
        localId = auth.get_account_info(user['idToken'])['users'][0]['localId']
    except:
        return render_template('login.html')

    sentences = db.child(localId).get().val()

    ori_sen = list(sentences.items())
    for sen in ori_sen:
        s = sen[1]
        for e in s.keys():
            for k in s[e].keys():
                lt.append((k, s[e][k]))

    return render_template('flashcards.html', flashcards=lt)
=======
    localID = auth.get_account_info(user['idToken'])
    user_data = db.child(localID).get()
    for entry in user_data.each():
        sentence = entry.
    
    return render_template('flashcards.html', flashcards=[('word', 'definition')])
>>>>>>> 5a82c6f98c09f36aa2a07cf99d0bd09e4faadfaa


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
