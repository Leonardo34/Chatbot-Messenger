import os
import sys
import json
import requests

def confirm_guest(guest):
    
    params = {
        "name":
        "last_name":
        "email":
        "phone":
        "optin":
        "rsvps[][event_id]":
        "rsvps[][adults]":
        "rsvps[][children]":
        "rsvps[][status]": 
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
        "X-User-Email": "leo_broch@hotmail.com"
        "X-User-Token": "ZB57obeHEyEkGW7fu2da"
        "Cache-Control": "no-cache"
    } 	
    r = requests.post("http://staging.mecasei.com/api/v2/wedding/51751/guests", params=params, headers=headers)