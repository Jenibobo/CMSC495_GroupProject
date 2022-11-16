from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
import urllib.request
import json

# Create your views here.
def current_weatherView(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid="your api_key here "  '''

        # current weather source containing json data from api
        current = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + 
            city + 
            '&appid=48a90ac42caa09f90dcaeee4096b9e53&units=imperial').read()

        forecast = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/forecast?q=' + 
            city + 
            '&appid=48a90ac42caa09f90dcaeee4096b9e53&cnt=5&units=imperial').read()


        # JSON data to dictionary
        try:
            current_w_data = json.loads(current)
            forecast_w_data = json.loads(forecast)

            # print(forecast_w_data)
            for i in forecast_w_data['list']:
                print(i['dt_txt'])
                print(i['main']['temp_min'])
                print(i['main']['temp_max'])
                print(i['weather'][0]['description'])
                print(i['weather'][0]['icon'])
                print('\n')

                # date_day = i['dt_txt']
            
            data = {
                "country_code": str(current_w_data['sys']['country']),
                "coordinate": str(current_w_data['coord']['lon']) + ' ' + str(current_w_data['coord']['lat']),
                "temp": str(current_w_data['main']['temp']) + u'\N{DEGREE SIGN}' + 'F',
                "humidity": str(current_w_data['main']['humidity']),
                "name": str(current_w_data['name']),
                "discrpition": str(current_w_data['weather'][0]['description']),
                "icon": str(current_w_data['weather'][0]['icon']),                
            }
            
        except ValueError:
            raise SuspiciousOperation('Invailid JSON')
    else:
        data={}
    return render(request, "weather.html", data)
