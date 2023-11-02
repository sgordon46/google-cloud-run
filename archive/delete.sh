#!/bin/bash

REPO=my-tomcat-2023
DIR=django_hl7_rest_api
IMAGE=my-tomcat-image-2023

gcloud artifacts repositories delete $REPO --location us-central1 --quiet #--async

docker rmi $IMAGE:latest
docker rmi us-central1-docker.pkg.dev/project1-366201/$REPO/$IMAGE:latest



rm -rf $DIR/Dockerfile $DIR/app_embedded_embed_app-name.zip $DIR/twistlock_defender_app_embedded.tar.gz

mv $DIR/Dockerfile.orig $DIR/Dockerfile

