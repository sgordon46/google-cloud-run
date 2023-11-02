import requests
import os

TOKEN = os.environ['TOKEN']
console_url = os.environ['PCC_API']
application_name = os.environ['application_name']

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


response = requests.post(console_url+"/api/v1/collections",
                         headers=pccHeaders, json=payload)
# print(response)
