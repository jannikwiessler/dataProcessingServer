"""web_service module.

This module simulates the WebService host for the trip data passed by a client

Example:
    To run the WebService manually one call in a proper command line:

        $ python web_service.py

__main__:
    Calls cherrypy.quickstart with the created config containing username and password
    to protect the application with auth_basic

"""
import cherrypy
from cherrypy.lib import auth_basic  # pylint: disable=unused-import
from trip_processor import TripProcessor

USERS = {'user1': 'pass1', 'user2': 'pass2'}


def validate_password(realm, username, password):  # pylint: disable=unused-argument
    """Method called by cherrypy to determine if clients request will be processed

    Args:
        string (username): Name of the user to log in
        string (password): Userspecific password
    """
    if username in USERS and USERS[username] == password:
        return True
    return False


class WebService():  # pylint: disable=too-few-public-methods
    """Class to host the WebService for processing incoming trip data."""
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def trip(self):  # pylint: disable=no-self-use
        """Method takes data from client
        and starts an instance of `dataProcessingServer.trip_processor.TripProcessor`
        as the engine.

        Error 400 will be thrown if the passed datatype is not valid.

        Runs data evaluation.

            Returns:
                dict: Analyzed trip data containing
                    int: vin
                    dict: departure
                    dict: destination
                    int: refuelStops
                    double: consumption
                    int: breaks
        """
        try:
            trip_data_processing_engine = TripProcessor(cherrypy.request.json)
        except AttributeError as exeption:
            raise cherrypy.HTTPError(status=400) from exeption
        trip_data_processing_engine.run()

        return trip_data_processing_engine.get_vehicle_push_analysis()


if __name__ == '__main__':
    config = {
        '/trip': {
            'tools.auth_basic.on': True,
            'tools.auth_basic.realm': 'trip',
            'tools.auth_basic.checkpassword': validate_password,
            'tools.auth_basic.accept_charset': 'UTF-8', }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(WebService(), '/', config)
