#!/usr/bin/env bash

EXERCISE_ID=67736b20-56e3-4f0a-bfb2-c96511312d4b

docker build --no-cache --label=pytm.exercise="$EXERCISE_ID" -t $EXERCISE_ID .
docker stop $EXERCISE_ID && docker rm $EXERCISE_ID
docker run -p 8000:8080 -d --name $EXERCISE_ID $EXERCISE_ID:latest
