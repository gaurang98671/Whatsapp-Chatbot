from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import weather

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!!!!!"

@app.route("/sms", methods=['POST'])
def sms_reply():

    """Respond to incoming calls with a simple text message."""
    # Fetch the message

    msg = request.form.get('Body')
    #check the message by parsing text
    resp = MessagingResponse()
    resp.message(weather.get_weather(msg))
    # Create reply
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)