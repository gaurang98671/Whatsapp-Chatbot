from flask import Flask, request, render_template, redirect, url_for
from twilio.twiml.messaging_response import MessagingResponse
import time
import reply


app = Flask(__name__)

@app.route("/")

def hello():
    return render_template('signup.html', title="SignUp")

@app.route('/signUp', methods=['POST'])

def signUp():
    username=str(request.form['user'])
    print(username)
    return redirect(url_for("login"))

@app.route('/login', methods=['POST', 'GET'])

def login():
    return render_template('login.html', data='Login')

@app.route('/login_user', methods=['POST'])
def login_user():
    userName=str(request.form['username'])
    password=str(request.form['password'])

    if(userName=="Gaurang" and password=="password"):
        return redirect(url_for('home'))
    else:
        return "Login failed"

@app.route("/home", methods=['GET'])
def home():
   return render_template('home.html')

@app.route("/sms", methods=['GET','POST'])

def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')


    #check the message by parsing text
    resp = MessagingResponse()
    #resp.message(reply.reply_message(msg))

    resp.message(reply.reply_message(msg))

    # Create reply
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)