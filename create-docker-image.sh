#!/bin/bash

REPO=my-tomcat-2023
IMAGE=my-tomcat-image-2023
DIR=django_hl7_rest_api
APPID=my-tomcat-app-embedded


PCC_USER=$PCC_KEY
PCC_PASS=$PCC_SEC
PCC_URL=$PCC_API
PCC_SAN="us-west1.cloud.twistlock.com"


#This  command will generate an authorization token (Only valid for 1 hour)
json_auth_data="$(printf '{ "username": "%s", "password": "%s" }' "${PCC_USER}" "${PCC_PASS}")"
token=$(curl -sSLk -d "$json_auth_data" -H 'content-type: application/json' "$PCC_URL/api/v1/authenticate" | python3 -c 'import sys, json; print(json.load(sys.stdin)["token"])')

echo -e $token

#The following variables can be set to customize the embedded function 
DATA="/data"


generate_post_data()
{
cat <<EOF
{
    "appID":"$APPID",
    "dataFolder":"$DATA",
    "consoleAddr":"$PCC_SAN",
    "filesystemMonitoring": true,
    "dockerfile":$(jq -Rs . <$DIR/Dockerfile)
}
EOF
}

echo -e $(generate_post_data)

echo -e "Generating embedded source file "

#Generate protected task
curl -sSLk   -H "Authorization: Bearer ${token}" "${PCC_URL}/api/v1/defenders/app-embedded" -X POST --data-raw "$(generate_post_data)" --output $DIR/app_embedded_embed_app-name.zip 

#mv $DIR/Dockerfile $DIR/Dockerfile.orig

unzip -o $DIR/app_embedded_embed_app-name.zip -d $DIR





