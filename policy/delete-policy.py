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
    'system': False

}


response = requests.get(
    console_url+"/api/v1/policies/runtime/app-embedded", headers=pccHeaders)

original_policy = response.json()
new_policy = original_policy

i = 0
match = None
for r in new_policy["rules"]:
    if r["name"] == application_name:
        match = i
    i += 1

if match is not None:
    print(match)
    del new_policy["rules"][match]
# new_policy["rules"].append(app_policy)

response = requests.put(
    console_url+"/api/v1/policies/runtime/app-embedded", headers=pccHeaders, json=new_policy)

# print(response)
