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
