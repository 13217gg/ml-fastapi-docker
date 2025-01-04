#!/bin/bash
if [ $# -ne 1 ]; then
    echo "No port number provided. Please provide the localhost port number you want to use for this container as argument"
    exit 1
fi

docker run -it --rm -p $1:12347 mlfastapidocker 

