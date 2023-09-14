#!/bin/bash

REPO=my-tomcat-2023
IMAGE=my-tomcat-image-2023



docker build -t $IMAGE django_hl7_rest2_api/.

docker tag $IMAGE:latest us-central1-docker.pkg.dev/project1-366201/$REPO/$IMAGE:latest



