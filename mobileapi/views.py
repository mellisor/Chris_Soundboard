from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os

# Create your views here.

base = os.path.join(settings.STATIC_ROOT,'home/Sounds')

def index(request):

    contents = os.listdir(base)
    data = {'categories' : contents}
    for tab in contents:
        data[tab] = os.listdir(os.path.join(base,tab))
    return JsonResponse(data)
