from datetime import datetime
from urllib.error import HTTPError
from django.shortcuts import redirect, render
from django.core.exceptions import SuspiciousOperation
import urllib.request
import datetime
import json
import math


# Create your views here.
def forecast(request):
    current_day = datetime.datetime.today()
    day2 = current_day + datetime.timedelta(days=1)
    day3 = current_day + datetime.timedelta(days=2)
    day4 = current_day + datetime.timedelta(days=3)
    day5 = current_day + datetime.timedelta(days=4)
    if request.method == 'POST':
        city = request.POST['city']

        weather_forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?q=' + city +'&APPID=3192803383f0bd308ae250f29d55a9a2&units=imperial'
        current_conditions_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53&units=imperial'
        
    
        weather_forecast = urllib.request.urlopen(weather_forecast_url)
        current_conditions = urllib.request.urlopen(current_conditions_url)
        try:
            # Pulling current weather condtions
            current_w_data = json.loads(current_conditions.read())
            current_data = {
                "country_code": str(current_w_data['sys']['country']),
                "cur_temp": str(current_w_data['main']['temp']) + u'\N{DEGREE SIGN}' + 'F',
                "feels_like": str(current_w_data['main']['feels_like']) + u'\N{DEGREE SIGN}' + 'F',
                "name": str(current_w_data['name']),
                "cur_discrpition": str(current_w_data['weather'][0]['description']).capitalize(),
                "cur_icon": str(current_w_data['weather'][0]['icon']),                
            }

            # Pulling data for the 5-day forecast
            w_dataset = json.loads(weather_forecast.read())
            data = {
                "city_name": w_dataset["city"]["name"],
                'date': w_dataset['list'][0]["dt_txt"],
                'date1': w_dataset['list'][1]["dt_txt"],
                'current_day':current_day.strftime('%A'),
                'day2':day2.strftime('%A'),
                'day3': day3.strftime('%A'),
                'day4': day4.strftime('%A'),
                'day5': day5.strftime('%A'),

                "temp": round(w_dataset["list"][0]["main"]["temp"]),
                "temp_min1": str(math.floor(w_dataset["list"][1]["main"]["temp_min"])) + u'\N{DEGREE SIGN}' + 'F',
                "temp_max1": str(math.ceil(w_dataset["list"][1]["main"]["temp_max"])) + u'\N{DEGREE SIGN}' + 'F',
                "temp_min2": str(math.floor(w_dataset["list"][2]["main"]["temp_min"])) + u'\N{DEGREE SIGN}' + 'F',
                "temp_max2": str(math.ceil(w_dataset["list"][2]["main"]["temp_max"])) + u'\N{DEGREE SIGN}' + 'F',
                "temp_min3": str(math.floor(w_dataset["list"][3]["main"]["temp_min"])) + u'\N{DEGREE SIGN}' + 'F',
                "temp_max3": str(math.ceil(w_dataset["list"][3]["main"]["temp_max"])) + u'\N{DEGREE SIGN}' + 'F',
                "temp_min4": str(math.floor(w_dataset["list"][4]["main"]["temp_min"])) + u'\N{DEGREE SIGN}' + 'F',
                "temp_max4": str(math.ceil(w_dataset["list"][4]["main"]["temp_max"])) + u'\N{DEGREE SIGN}' + 'F',
                "temp_min5": str(math.floor(w_dataset["list"][5]["main"]["temp_min"])) + u'\N{DEGREE SIGN}' + 'F',
                "temp_max5": str(math.ceil(w_dataset["list"][5]["main"]["temp_max"])) + u'\N{DEGREE SIGN}' + 'F',

                "icon": w_dataset["list"][0]["weather"][0]["icon"],
                "icon1": w_dataset["list"][1]["weather"][0]["icon"],
                "icon2": w_dataset["list"][2]["weather"][0]["icon"],
                "icon3": w_dataset["list"][3]["weather"][0]["icon"],
                "icon4": w_dataset["list"][4]["weather"][0]["icon"],
                "icon5": w_dataset["list"][5]["weather"][0]["icon"],
            }
            data['current_condtions'] = current_data
        except Exception as e:
            print(e)
    else:
        data = {}
    return render(request, "weatherforecast.html", data)
