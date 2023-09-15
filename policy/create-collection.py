import requests
import os

console_url = os.getenv("PCC_API")
access_key = os.getenv("PCC_KEY")
secret_key = os.getenv("PCC_SEC")

application_name = os.getenv("application_name")

payload = {
    'username': access_key,
    'password': secret_key
}

# Generate a Token for access to Prisma Cloud Compute.
TOKEN = requests.post(console_url+"/api/v1/authenticate",json=payload).json()['token']

# Set Prisma Cloud Headers for Login with token
pccHeaders = {
    'Authorization': 'Bearer '+TOKEN,
    'Accept': 'application/json'
}

payload = {
    "name": application_name,
    "description": application_name,
    'appIDs': [application_name+"*"],
    'containers': ["*"],
    'images': ["*"],
    'system': False

}

# print(payload)


response = requests.post(console_url+"/api/v1/collections",headers=pccHeaders, json=payload)
# print(response)
