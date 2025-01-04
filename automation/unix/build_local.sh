#!/bin/bash

docker build  --build-arg DISABLE_SSL_FOR_PIP=1 -t mlfastapidocker -f docker/Dockerfile .

