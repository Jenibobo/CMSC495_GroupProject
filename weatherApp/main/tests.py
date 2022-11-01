from django.test import TestCase

# Create your tests here.
mock_data = {
    'coord': 
    {
        'lon': -96.7836, 
        'lat': 32.7668
    }, 
    'weather': 
    [
        {
            'id': 802, 
            'main': 'Clouds', 
            'description': 
            'scattered clouds', 
            'icon': '03d'
        }
    ], 
    'base': 'stations', 
    'main': 
    {
        'temp': 291.78, 
        'feels_like': 291.68, 
        'temp_min': 289.42, 
        'temp_max': 294.82, 
        'pressure': 1022, 
        'humidity': 76
    }, 
    'visibility': 10000, 
    'wind': 
    {
        'speed': 1.54, 
        'deg': 150
    }, 
    'clouds': 
    {
        'all': 40
    }, 
    'dt': 1667316057, 
    'sys': 
    {
        'type': 2, 
        'id': 2075302, 
        'country': 'US', 
        'sunrise': 1667306690, 
        'sunset': 1667345788
    }, 
    'timezone': -18000, 
    'id': 4684904, 
    'name': 'Dallas', 
    'cod': 200
}
