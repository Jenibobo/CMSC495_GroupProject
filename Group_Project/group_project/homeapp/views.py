from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
import urllib.request
import json


def index(request):
    return render(request, 'base.html')
