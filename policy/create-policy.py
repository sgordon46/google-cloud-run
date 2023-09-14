import requests
import json

console_url   = "https://us-west1.cloud.twistlock.com/us-4-161024557"
access_key     = "f0f68363-a032-47e4-88d7-055a7e5b819d"
secret_key    = "HZ8uaAjrvy76jUzN3QB1TIi2eVk="

application_name = "my-tomcat-app-embedded"

payload = {
    'username':access_key,
    'password':secret_key
}

#Generate a Token for access to Prisma Cloud Compute. 
TOKEN = requests.post(console_url+"/api/v1/authenticate", json=payload).json()['token']

#Set Prisma Cloud Headers for Login with token
pccHeaders = {
    'Authorization': 'Bearer '+TOKEN,
    'Accept': 'application/json'
}

payload = {
    "name": application_name,
    "description":application_name,
    'appIDs':[application_name+"*"],
    'system':False

}

f = open("app-policy.json","r")
app_policy = json.loads(f.read())
f.close()

#print(app_policy)

response = requests.get(console_url+"/api/v1/policies/runtime/app-embedded", headers=pccHeaders)

original_policy = response.json()
new_policy = original_policy

#del new_policy["rules"][1]
new_policy["rules"].append(app_policy)

response = requests.put(console_url+"/api/v1/policies/runtime/app-embedded", headers=pccHeaders, json=new_policy)

print(response)