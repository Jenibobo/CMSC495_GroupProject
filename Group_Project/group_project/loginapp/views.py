from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def loginView(request):
    print("")
    return render(request, 'login.html')



