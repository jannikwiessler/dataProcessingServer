#!/bin/bash
# this is linux specific  
# https://get.docker.com requires admin username and password and is destripution sensitive

if ! [[ "$(command -v docker)" == *"docker"* ]]; then
  # install docker
    curl -fsSL https://get.docker.com | sh
fi

# clone repo
git clone https://github.com/jannikwiessler/dataProcessingServer.git dataProcessingServer

# change directory
cd dataProcessingServer

# run docker 
docker build -t python-webservice .
docker run -d --name webservice -p 8080:8080 python-webservice