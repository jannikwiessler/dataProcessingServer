"""unit test module.

This module contains a Class to test the
`dataProcessingServer.trip_processor.TripProcessor` methods.

__main__:
    unittest.run to perform the tests.

"""
import unittest
from copy import deepcopy
from parameterized import parameterized
from test_data import test_data
from trip_processor import TripProcessor


class TripDataProcessorTest(unittest.TestCase):
    # pylint: disable=no-self-use
    """Class containing specific unit tests for
    `dataProcessingServer.trip_processor.TripProcessor` methods.
    """

    @parameterized.expand([
        ["vin", -1.0],
        ["breakThreshold", "invalidData"],
        ["data", -1.0]
    ])
    def test_trip_processor_check_data_format_invalid_data(self, key, invalid_data):
        """
        Method to test
        `dataProcessingServer.trip_processor.TripProcessor`'s __check_data_format()
        In Practice we do not test private methods: this is only for demonstration
        Test is classified as correct if error is thrown
        ----------
        """
        invalid_test_data = deepcopy(test_data)
        invalid_test_data[key] = invalid_data
        with self.assertRaises(DataNotInValidFormatError, msg=key):
            # call contructor within check_data_format()
            TripProcessor(invalid_test_data)


if __name__ == '__main__':
    unittest.main()
