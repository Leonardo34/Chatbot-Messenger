import os
import sys
import json
import requests
from app import log

def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": "EAAD9zMOLhhIBAO9LUAwaIeZB86tZBfsH0pMTx3ZAkHiOhN6BQ1U3LbHaH7oDnSs4R9g1ZC0vINZCIkkRT8iEWZAkokGp035c83ZAoOpzw127KJLjZAJPeyhXl708zw6cmLZBjs6RXizkwPVJd6NIrbP1ptEnsJi8Hw742AS3kjAoYmgZDZD"
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)