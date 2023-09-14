#!/bin/bash

REPO=my-tomcat-2023

gcloud artifacts repositories delete $REPO --location us-central1 --quiet #--async

docker rmi  $IMAGE 
docker rmi  us-central1-docker.pkg.dev/project1-366201/$REPO/$IMAGE:latest



#rm -rf Dockerfile app_embedded_embed_app-name.zip twistlock_defender_app_embedded.tar.gz

#mv Dockerfile.orig Dockerfile

