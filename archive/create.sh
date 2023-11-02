#!/bin/bash

REPO=my-tomcat-2023
IMAGE=my-tomcat-image-2023
DIR=django_hl7_rest_api

PCC_USER=""
PCC_PASS=""
PCC_URL=""
PCC_SAN=""


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

mv $DIR/Dockerfile $DIR/Dockerfile.orig

unzip $DIR/app_embedded_embed_app-name.zip -d $DIR



gcloud artifacts repositories create $REPO --location us-central1 --repository-format=docker --quiet #--async

docker build -t $IMAGE $DIR/.

docker tag $IMAGE:latest us-central1-docker.pkg.dev/project1-366201/$REPO/$IMAGE:latest

docker push us-central1-docker.pkg.dev/project1-366201/$REPO/$IMAGE:latest


