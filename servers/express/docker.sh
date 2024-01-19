#!/bin/zsh

PORT="$1"
NAME="express"

if [ "$PORT" == "" ]; then
  PORT="3000"
fi

docker build . -t $NAME

if [ "$(docker container inspect --format '{{.Name}}' $NAME 2>&1)" == "/$NAME" ]; then
  docker rm -f $NAME
fi

docker run \
  --name $NAME -d \
  -p $PORT:3000 \
  express