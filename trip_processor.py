"""trip processor module.
This module contains Classes to perform the data evaluation to return analyzed vehicle data

"""
from copy import deepcopy  # to secure original data
from geopy.geocoders import Nominatim  # for location map


class TripProcessor:
    """Class to perform the data evaluation to return analyzed vehicle data
    """

    def __init__(self, data):
        """Constructor creates a new instance of this class
        Args:
            dict (data) : data passed by client 
        """
        self.__depature_location = dict()
        self.__destination_location = dict()
        self.__breaks = list()
        self.__refuel_stops = list()
        self.__consumption = float()
        self.__trip_data = dict()

        self.__trip_data = data

    def __map_depature_destination_location(self):
        single_timestamp = self.__get_single_timestamp_by_index(0)  # depature
        self.__depature_location = self.__get_location_by_timestamp(
            single_timestamp)  # this is dict
        # destination
        single_timestamp = self.__get_single_timestamp_by_index(-1)
        self.__destination_location = self.__get_location_by_timestamp(
            single_timestamp)  # this is dict

    def __get_location_by_timestamp(self, single_timestamp):
        geolocator = Nominatim(user_agent="geoapiExercises")
        geo_string = str(
            single_timestamp['positionLat'])+","+str(single_timestamp['positionLong'])
        return geolocator.reverse(geo_string).raw['address']

    def __get_single_timestamp_by_index(self, index=0):
        return self.__trip_data['data'][index]  # protect the original data

    def __get_data_over_timestamps(self, label="fuelLevel"):
        # assume proper data preprocessing: no missing data here
        data_over_timestamps = [d[label] for d in self.__trip_data['data']]
        # assume proper data preprocessing: data has same length
        timestamp = [d['timestamp'] for d in self.__trip_data['data']]
        return timestamp, data_over_timestamps

    def __calc_breaks_and_refuels(self, threshold_time_break=1800):
        timestamps, fuel_level_over_timestamps = self.__get_data_over_timestamps(
            'fuelLevel')
        # assuming engine off via breaks/refueling: therefore no timestamp counter incementation
        for i in range(len(timestamps)-1):
            breaking = timestamps[i+1] > timestamps[i]+threshold_time_break
            refueling = fuel_level_over_timestamps[i +
                                                   1] > fuel_level_over_timestamps[i]
            # unix time incremented in seconds: assume break of at least 1800 seconds
            # (want not to detect engine off on Railroad Crossing)
            if breaking or refueling:
                temp = {"startTimestamp": timestamps[i],
                        "endTimestamp": timestamps[i+1],
                        "positionLat": self.__get_single_timestamp_by_index(i)['positionLat'],
                        "positionLong": self.__get_single_timestamp_by_index(i)['positionLong']
                        }  # for debugging cases
                self.__breaks.append(temp)
                if refueling:
                    self.__refuel_stops.append(temp)

    def __calc_consuption(self):
        _, fuel_level_over_timestamps = self.__get_data_over_timestamps(
            'fuelLevel')
        _, odometer_over_timestamps = self.__get_data_over_timestamps(
            'odometer')
        total_km = odometer_over_timestamps[-1]-odometer_over_timestamps[0]
        total_consumption = 0
        for i in range(len(fuel_level_over_timestamps)-1):
            consumption = fuel_level_over_timestamps[i] - \
                fuel_level_over_timestamps[i+1]
            if consumption > 0:
                total_consumption = total_consumption + consumption
        if total_consumption == 0:
            self.__consumption = 0
        elif total_km == 0:  # running engine without moving the car --> -1 indicates this edge case
            self.__consumption = -1
        else:
            self.__consumption = total_consumption/(total_km/100)

    def get_depature_location(self):
        """Getter for depature location
        Returns:
            dict: location of depature from geolocator.reverse() as deepcopy
        """
        return deepcopy(self.__depature_location)  # protect the original data

    def get_destination_location(self):
        """Getter for destination location
        Returns:
            dict: location of destination from geolocator.reverse() as deepcopy
        """
        return deepcopy(self.__destination_location)  # protect the original data

    def get_vehicle_identification_number(self):
        """Getter for vehicle identification number
        Returns:
            string: vin as deepcopy
        """
        return deepcopy(self.__trip_data['vin'])  # protect the original data

    def get_breaks(self):
        """Getter for breaks
        Returns:
            array: containing dictionaries within the break
            start and end timestamps as deepcopy
        """
        return deepcopy(self.__breaks)  # protect the original data

    def get_refuel_stops(self):
        """Getter for refuel stops
        Returns:
            array: containing dictionaries within the refuel stops
            start and end timestamps as deepcopy
        """
        return deepcopy(self.__refuel_stops)  # protect the original data

    def get_consuption(self):
        """Getter for consumption
        Returns:
            float: over trip calculated km specific fuel consumption as deepcopy
        """
        return deepcopy(self.__consumption)  # protect the original data

    def run(self):
        """Runs the engins data processing methods.

        Stores the resulting calculations for

        - depature and destination location

        - breaks and refuel stops

        - consumption

        in corresponding privat attributes.
        """
        self.__map_depature_destination_location()  # unzip depature and destination
        self.__calc_breaks_and_refuels()
        self.__calc_consuption()

    def get_vehicle_push_analysis(self):
        """Getter for final analyzed tip data as deepcopy

        As specified in *swagger-task.yml*:

            Returns:
                dict: Analyzed trip data containing
                    int: vin
                    dict: departure
                    dict: destination
                    int: refuelStops
                    double: consumption
                    int: breaks

        """
        temp = {"vin": self.get_vehicle_identification_number(),
                "departure": self.get_depature_location()['city'],
                "destination": self.get_destination_location()['city'],
                "refuelStops": self.get_refuel_stops(),
                "consumption": self.get_consuption(),
                "breaks": self.get_breaks()
                }  # for debugging cases
        return temp
