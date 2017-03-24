import os
import sys
import json
import requests

import facebookApi
from flask import Flask, request

app = Flask(__name__)

guests = []

@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "irineu_nem_eu":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data) 

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):

                    sender_id = messaging_event["sender"]["id"] 
                    recipient_id = messaging_event["recipient"]["id"]  
                    message_text = messaging_event["message"]["text"]

                    response = parse_message(message_text)  

                    send_message(sender_id, response)

                if messaging_event.get("delivery"):
                    pass

                if messaging_event.get("optin"):
                    pass

                if messaging_event.get("postback"):
                    pass

    return "ok", 200


def log(message):
    print str(message)
    sys.stdout.flush()

def parse_message(message_text):
    if message_text[:5] == "#nome"
        return "Nome Cadastrado"
    return "Desculpa, não entendi"      


if __name__ == '__main__':
    from facebookApi import send_message
    app.run(debug=True)
