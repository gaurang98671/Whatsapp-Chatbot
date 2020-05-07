from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!!!!!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    list=[]
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    if(msg=="Hello"):
        resp = MessagingResponse()
        resp.message("Hello, what is your name")
    # Create reply
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)