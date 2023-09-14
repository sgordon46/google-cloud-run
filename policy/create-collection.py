import requests

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
    'containers':["*"],
    'images':["*"],
    'system':False

}

#print(payload)


response = requests.post(console_url+"/api/v1/collections", headers=pccHeaders, json=payload)
#print(response)


