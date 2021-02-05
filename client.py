"""client module.
This module represents an exsample of a client to pass trip data
to a hosted `dataProcessingServer.web_service.WebService` instance.
Caller will be asked for valid username and password.
Generic data `dataProcessingServer.test_data`
Example:
    To run the client script manually one call in the command line:

        $ python client.py

"""
import getpass
import requests
from test_data import test_data

if __name__ == '__main__':
    # pass request
    URL = 'http://localhost:8080/trip'

    USERNAME = str(input("username: "))
    PASSWORD = str(getpass.getpass("password: ", stream=None))

    response = requests.post(URL, json=test_data, auth=(USERNAME, PASSWORD))
    # check for internal server error
    if response.status_code == 200 or response.status_code == 500:
        print(response.status_code)
        print(response.text)
    else:
        print(response.status_code)
