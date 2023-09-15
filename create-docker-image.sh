#!/bin/bash

REPO=my-tomcat-2023
IMAGE=my-tomcat-image-2023
DIR=django_hl7_rest_api

PCC_USER="f0f68363-a032-47e4-88d7-055a7e5b819d"
PCC_PASS="HZ8uaAjrvy76jUzN3QB1TIi2eVk="
PCC_URL="https://us-west1.cloud.twistlock.com/us-4-161024557"
PCC_SAN="us-west1.cloud.twistlock.com"


#This  command will generate an authorization token (Only valid for 1 hour)
json_auth_data="$(printf '{ "username": "%s", "password": "%s" }' "${PCC_USER}" "${PCC_PASS}")"
token=$(curl -sSLk -d "$json_auth_data" -H 'content-type: application/json' "$PCC_URL/api/v1/authenticate" | python3 -c 'import sys, json; print(json.load(sys.stdin)["token"])')

echo -e $token

#The following variables can be set to customize the embedded function 
APPID=$REPO
DATA="/data"

#FILE="$(<Dockerfile)"

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


#gcloud artifacts repositories create $REPO --location us-central1 --repository-format=docker --quiet #--async


#docker build -t us-central1-docker.pkg.dev/project1-366201/$REPO/$IMAGE:latest $DIR/.

#docker push us-central1-docker.pkg.dev/project1-366201/$REPO/$IMAGE:latest


