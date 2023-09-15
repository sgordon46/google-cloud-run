import requests
import json
import os

console_url = os.environ["PCC_API"]
access_key = os.environ["PCC_KEY"]
secret_key = os.environ["PCC_SEC"]

application_name = os.environ["application_name"]

payload = {
    'username': access_key,
    'password': secret_key
}

# Generate a Token for access to Prisma Cloud Compute.
TOKEN = requests.post(console_url+"/api/v1/authenticate",
                      json=payload).json()['token']

# Set Prisma Cloud Headers for Login with token
pccHeaders = {
    'Authorization': 'Bearer '+TOKEN,
    'Accept': 'application/json'
}

payload = {
    "name": application_name,
    "description": application_name,
    'appIDs': [application_name+"*"],
    'system': False

}

f = open("policy/app-policy.json", "r")
app_policy = json.loads(f.read())
f.close()

app_policy["name"] = application_name
app_policy["collections"]["appIDs"] = [application_name+"*"]
app_policy["collections"]["name"] = application_name
app_policy["collections"]["description"] = application_name


# print(app_policy)

response = requests.get(console_url+"/api/v1/policies/runtime/app-embedded", headers=pccHeaders)

original_policy = response.json()
new_policy = original_policy

# del new_policy["rules"][1]
new_policy["rules"].append(app_policy)

response = requests.put(console_url+"/api/v1/policies/runtime/app-embedded", headers=pccHeaders, json=new_policy)

print(response)
