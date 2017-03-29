import os
import sys
import json
import requests

import model
import facebookApi
from flask import Flask, request


app = Flask(__name__)
EVENT_ID = "teste"
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

                    response = parse_message(message_text, sender_id)  

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


def parse_message(message_text, sender_id):
    guest = find_guest(sender_id)

    if message_text[:5] == "#nome":
        names = message_text.split(" ")
        first_name = names[1]
        last_name = names[2]
        guest.set_name(first_name)
        guest.set_last_name(last_name)
        print guest.name
        return "Nome Cadastrado"

    if message_text[:6] == "#email":
        guest.set_email(message_text[7:-1])
        print guest.name
        return "Email Cadastrado"

    if message_text[:9] == "#telefone":
        guest.set_phone(message_text[10:-1])
        print guest.name
        return "Telefone Cadastrado"

    if message_text[:9] == "#crianças":  
        guest.set_childrens(message_text[10:-1])
        return "Suas crianças foram confirmadas :)"

    if message_text[:8] == "#adultos":
        guest.set_adults(message_text[9:-1])
        return "Voce confirmou a presença de {} adultos".format(guest.adults)

    if message_text[:6] == "#euvou":
        confirm_guest(guest, "attend", EVENT_ID)

    if message_text[:7] == "#naovou":
        confirm_guest(guest, "not_attend", EVENT_ID)               

    return "Ola, voce pode confirmar suas informaçoes atraves das hashtags #nome, #telefone, #email, #crianças e #adultos. Para confirmar presença ou rejeitar, diga #euvou ou #naovou"


def find_guest(sender_id):
    for guest in guests:
        if guest.id == sender_id:
            return guest

    new_guest = Guest(sender_id)
    guests.append(new_guest)
    return new_guest                   


if __name__ == '__main__':
    from facebookApi import send_message
    from model import Guest
    from mecaseiApi import confirm_guest
    app.run(debug=True)
