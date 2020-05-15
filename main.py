from flask import Flask, request, render_template, redirect, url_for
from twilio.twiml.messaging_response import MessagingResponse
import time
import reply


app = Flask(__name__)

@app.route("/")

def hello():
    return render_template("Hello world")



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