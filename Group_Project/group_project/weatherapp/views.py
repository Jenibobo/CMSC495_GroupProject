from datetime import datetime
from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
import urllib.request
import json

# Create your views here.
def current_weatherView(request):
    if request.method == 'POST':
        city = request.POST['city']
        # state = request.POST['state']

        # The apis are requesting data for weather, and returned in a JSON 
        # format.

        # current weather 
        current = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + 
            city +
            '&appid=48a90ac42caa09f90dcaeee4096b9e53&units=imperial').read()

        # forecasted weather for the next 5 days every 3 hours
        forecast = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/forecast/?q=' + 
            city + 
            '&appid=48a90ac42caa09f90dcaeee4096b9e53&units=imperial').read()


        # JSON data to dictionary
        try:
            current_w_data = json.loads(current)
            forecast_w_data = json.loads(forecast)

            forecast_weather = {}
            date_format = "%A %b %d %Y"
            time_format = "%I %p"

            for i in forecast_w_data['list']:
                day = i['dt_txt'].split(' ')

                # Turning date into date obj to change format that will be 
                # displayed.
                date_obj = datetime.strptime(day[0], "%Y-%m-%d").date()
                forecast_date = date_obj.strftime(date_format)

                # # Turning time into time obj to change format that will be 
                # # displayed.
                time_obj = datetime.strptime(day[1], "%H:%M:%S").time()


                details = {
                        "time": time_obj.strftime(time_format),
                        "conditions": i['weather'][0]['main'],
                        "low": i['main']['temp_min'],
                        "high": i['main']['temp_max']
                }

                if forecast_date in forecast_weather:
                    forecast_weather[forecast_date].append(details)
                else:
                    forecast_weather.update({forecast_date:[details]})
            
            
            data = {
                "country_code": str(current_w_data['sys']['country']),
                "coordinate": str(current_w_data['coord']['lon']) + ' ' + str(current_w_data['coord']['lat']),
                "temp": str(current_w_data['main']['temp']) + u'\N{DEGREE SIGN}' + 'F',
                "humidity": str(current_w_data['main']['humidity']),
                "name": str(current_w_data['name']),
                "discrpition": str(current_w_data['weather'][0]['description']),
                "icon": str(current_w_data['weather'][0]['icon']),                
            }
            data['forecast'] = forecast_weather
            
        except ValueError:
            raise SuspiciousOperation('Invailid JSON')
    else:
        data={}
    return render(request, "weather.html", data)
