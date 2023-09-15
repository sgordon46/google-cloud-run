import requests
import os

console_url = os.environ['PCC_API']
access_key = os.environ['PCC_KEY']
secret_key = os.environ['PCC_SEC']

application_name = os.environ['application_name']

payload = {
    'username': access_key,
    'password': secret_key
}



# Generate a Token for access to Prisma Cloud Compute.
TOKEN = requests.post(console_url+'/api/v1/authenticate',json=payload).json()['token']

# Set Prisma Cloud Headers for Login with token
pccHeaders = {
    'Authorization': 'Bearer '+TOKEN,
    'Accept': 'application/json'
}

payload = {
    'name': application_name,
    'description': application_name,
    'appIDs': [application_name+'*'],
    'containers': ['*'],
    'images': ['*'],
    'system': False

}


response = requests.delete(console_url+'/api/v1/collections/'+application_name, headers=pccHeaders)
