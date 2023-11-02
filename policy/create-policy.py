import requests
import json
import os

TOKEN = os.environ['TOKEN']
console_url = os.environ['PCC_API']
application_name = os.environ['application_name']
SCRIPT = os.environ['SCRIPT']

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

f = open("policy/app-policy-"+SCRIPT+".json", "r")
app_policy = json.loads(f.read())
f.close()

app_policy["name"] = application_name
app_policy["collections"][0]["appIDs"][0] = application_name+"*"
app_policy["collections"][0]["name"] = application_name
app_policy["collections"][0]["description"] = application_name


# print(app_policy)

response = requests.get(
    console_url+"/api/v1/policies/runtime/app-embedded", headers=pccHeaders)

original_policy = response.json()
new_policy = original_policy

# del new_policy["rules"][1]
# insert policy as the first option in the list
new_policy["rules"].insert(0,app_policy)

response = requests.put(
    console_url+"/api/v1/policies/runtime/app-embedded", headers=pccHeaders, json=new_policy)

# print(response)
