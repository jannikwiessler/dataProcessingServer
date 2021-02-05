"""test_data dictionaray

This is used in `dataProcessingServer.client` to test the
`dataProcessingServer.trip_processor.TripProcessor` Class

This gerneic and therefore no meeningfull data.

"""
test_data = {
    "vin": "XYZ00000000123",
    "breakThreshold": 1800,
    "gasTankSize": 80,
    "data": [
        {
            "timestamp": 1559137020,
            "odometer": 7200,
            "fuelLevel": 52,
            "positionLat": 48.771990,
            "positionLong": 9.172787
        },
        {
            "timestamp": 1559137021,
            "odometer": 7201,
            "fuelLevel": 51,
            "positionLat": 48.7748376,
            "positionLong": 9.1876701
        },
        {
            "timestamp": 1559137022,
            "odometer": 7202,
            "fuelLevel": 50,
            "positionLat": 48.7748376,
            "positionLong": 9.1876701
        },
        {
            "timestamp": 1559137100,
            "odometer": 7203,
            "fuelLevel": 80,
            "positionLat": 48.7748376,
            "positionLong": 9.1876701
        },
        {
            "timestamp": 1559137026,
            "odometer": 7204,
            "fuelLevel": 79,
            "positionLat": 48.7748376,
            "positionLong": 9.1876701
        }
    ]
}
