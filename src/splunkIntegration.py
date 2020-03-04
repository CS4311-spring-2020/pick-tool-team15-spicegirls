from __future__ import absolute_import
from os import path
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import splunklib.client as client

HOST = "localhost"
PORT = 8089
USERNAME = "dimaaj"
PASSWORD = "@DimaAbdelJaber1234@"
OWNER = "dimaaj"       # Replace this with a valid username
APP   = "search"

# Create a Service instance and log in 
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD,
    owner=OWNER,
    app=APP)

# Print installed apps to the console to verify login
for app in service.apps:
    print (app.name)
