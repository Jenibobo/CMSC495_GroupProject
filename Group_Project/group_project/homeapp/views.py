from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
import urllib.request
import json


def index(request):
    return render(request, 'base.html')


# Create your views here.
def current_weatherView(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid="your api_key here "  '''

        # current weather source containing json data from api
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + 
            city + 
            '&appid=48a90ac42caa09f90dcaeee4096b9e53&units=imperial').read()

        # JSON data to dictionary
        try:
            list_of_data = json.loads(source)
            # print(list_of_data)

            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + u'\N{DEGREE SIGN}' + 'F',
                "humidity": str(list_of_data['main']['humidity']),
                "name": str(list_of_data['name']),
                "discrpition": str(list_of_data['weather'][0]['description']),
                "icon": str(list_of_data['weather'][0]['icon']),
            }
            
        except ValueError:
            raise SuspiciousOperation('Invailid JSON')
    else:
        data={}
    return render(request, "weather.html", data)


# def todoappView(request):
#     print('anything')
#     all_todo_items = TodoListItem.objects.all()
#     todos = {
#         "all_items": all_todo_items
#     }
#     print(todos)
#     print(all_todo_items)
#     return render(request, 'todo.html', todos)


# def add_todoView(request):
#     # print('anything')
#     x = request.POST['content']
#     new_item = TodoListItem(content = x)
#     new_item.save()
#     return HttpResponseRedirect('/homeapp/')


# def deleteTodoView(request, i):
#     y = TodoListItem.objects.get(id= i)
#     y.delete()
#     return HttpResponseRedirect('/homeapp/')