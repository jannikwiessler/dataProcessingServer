# dataProcessingServer

## Description

This repository contains a quickstart example with several topics of software engineering 

### 21.01.2021 including:

- [x] Implementation of REST Endpoint
- [x] Protection of the API with BasicAuth
- [x] Docker is used to run the application
- [x] Application is developed with Python
- [x] Automation of infrastructure rollout (git is required, this is for linux)
- [x] [Nominatim](https://nominatim.org/) is used as an external service to determine the city name for depature and destination
- [x] Examples for valid and invalid data sets are used for unit tests.

### Continuous Integration

**on_checkin_tasks.yml**:
 - Unit tests will be performed on github by checking in changes
 - Docker build will be tested by checking in changes
 - Analysing the code with pylint will be performed by checking in changes

## Usage

In order to use this repository you will need to make sure that the following dependencies are installed on your system:
  - Docker (if no automated infrastructure setup is used)
  - Git (even if automated infrastructure setup is used)

### Quickstart

On Linux one can download `setup_infrastructure.sh` and run it as administrator with `sudo ./setup_infrastructure.sh`

If no automated infrastructure rollout is used please clone the repo and call:
 - `docker build -t python-webservice .` to build the docker image `python-webservice` from the given dockerfile
 - `docker run -d --name webservice -p 8080:8080 python-webservice` to run the image as container `webservice`

To start the client by 'python client.py' please use one of the following users with its password:

username | password
------| -------------
user1 | pass1
user2 | pass2

As the client script is only set up to test the functionality of the web service a very generic data set will be passed to the WebService. 

 ### Data Processing
 
This simple example evaluates vehicle trip data passed from the client as json:
 - [x] Start & Stop location by given longitude and latitude
 - [x] Breaks and refueling stops
 - [x] Average consumption 

 There are three assumptions on which the calculation of breaks and refueling stops are based:
  - proper data preprocessing: no missing data in the passed datasets
  - assuming engine off via breaks/refueling: therefore no timestamp counter incementation
  - timestamp: unix time incremented in seconds
