from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.form.get('Body')
    response = MessagingResponse()
    msg = response.message()

    # Simple lógica para el chatbot
    if 'hola' in incoming_msg.lower():
        msg.body("¡Hola! ¿En qué puedo ayudarte hoy?")
    else:
        msg.body("Lo siento, no entiendo tu mensaje.")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
