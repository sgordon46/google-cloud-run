import requests
import json
import os

console_url = os.environ['PCC_API']
access_key = os.environ['PCC_KEY']
secret_key = os.environ['PCC_SEC']


payload = {
    'username': access_key,
    'password': secret_key
}

# Generate a Token for access to Prisma Cloud Compute.
TOKEN = requests.post(console_url+"/api/v1/authenticate",
                      json=payload).json()['token']


env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("TOKEN="+TOKEN)

