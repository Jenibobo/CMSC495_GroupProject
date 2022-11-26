from datetime import datetime
from django.shortcuts import render
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

        current = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/forecast?q='+city+'&APPID=3192803383f0bd308ae250f29d55a9a2&units=imperial').read()
        try:
            w_dataset = json.loads(current)
            data = {
                "city_name": w_dataset["city"]["name"],
                "city_country": w_dataset["city"]["country"],
                "wind": w_dataset['list'][0]['wind']['speed'],
                "degree": w_dataset['list'][0]['wind']['deg'],
                "status": w_dataset['list'][0]['weather'][0]['description'],
                "cloud": w_dataset['list'][0]['clouds']['all'],
                'date': w_dataset['list'][0]["dt_txt"],
                'date1': w_dataset['list'][1]["dt_txt"],
                'current_day':current_day.strftime('%A'),
                'day2':day2.strftime('%A'),
                'day3': day3.strftime('%A'),
                'day4': day4.strftime('%A'),
                'day5': day5.strftime('%A'),

                "temp": round(w_dataset["list"][0]["main"]["temp"]),
                "temp_min1": math.floor(w_dataset["list"][1]["main"]["temp_min"]),
                "temp_max1": math.ceil(w_dataset["list"][1]["main"]["temp_max"]),
                "temp_min2": math.floor(w_dataset["list"][2]["main"]["temp_min"]),
                "temp_max2": math.ceil(w_dataset["list"][2]["main"]["temp_max"]),
                "temp_min3": math.floor(w_dataset["list"][3]["main"]["temp_min"]),
                "temp_max3": math.ceil(w_dataset["list"][3]["main"]["temp_max"]),
                "temp_min4": math.floor(w_dataset["list"][4]["main"]["temp_min"]),
                "temp_max4": math.ceil(w_dataset["list"][4]["main"]["temp_max"] ),
                "temp_min5": math.floor(w_dataset["list"][5]["main"]["temp_min"] ),
                "temp_max5": math.ceil(w_dataset["list"][5]["main"]["temp_max"] ),

                "pressure": w_dataset["list"][0]["main"]["pressure"],
                "humidity": w_dataset["list"][0]["main"]["humidity"],
                "sea_level": w_dataset["list"][0]["main"]["sea_level"],

                "weather": w_dataset["list"][1]["weather"][0]["main"],
                "description": w_dataset["list"][1]["weather"][0]["description"],
                "icon": w_dataset["list"][0]["weather"][0]["icon"],
                "icon1": w_dataset["list"][1]["weather"][0]["icon"],
                "icon2": w_dataset["list"][2]["weather"][0]["icon"],
                "icon3": w_dataset["list"][3]["weather"][0]["icon"],
                "icon4": w_dataset["list"][4]["weather"][0]["icon"],
                "icon5": w_dataset["list"][5]["weather"][0]["icon"],}



        except ValueError:
            raise SuspiciousOperation('Invailid JSON')
    else:
        data = {}
    return render(request, "weatherforecast.html", data)
