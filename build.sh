#!/bin/bash

REPO=my-tomcat-2023
IMAGE=my-tomcat-image-2023



gcloud artifacts repositories create $REPO --location us-central1 --repository-format=docker --quiet #--async

docker build -t $IMAGE django_hl7_rest_api/.

docker tag $IMAGE:latest us-central1-docker.pkg.dev/project1-366201/$REPO/$IMAGE:latest

docker push us-central1-docker.pkg.dev/project1-366201/$REPO/$IMAGE:latest


