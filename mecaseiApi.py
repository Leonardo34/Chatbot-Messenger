import os
import sys
import json
import requests

def confirm_guest(guest, status, event_id):
    
    params = {
        "name": guest.name
        "last_name": guest.last_name
        "email": guest.email
        "phone": guest.phone
        "optin": guest.optin
        "rsvps[][event_id]": event_id
        "rsvps[][adults]": guest.adults
        "rsvps[][children]": guest.childrens
        "rsvps[][status]": status
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
        "X-User-Email": "leo_broch@hotmail.com"
        "X-User-Token": "ZB57obeHEyEkGW7fu2da"
        "Cache-Control": "no-cache"
    } 	
    r = requests.post("http://staging.mecasei.com/api/v2/wedding/51751/guests", params=params, headers=headers)