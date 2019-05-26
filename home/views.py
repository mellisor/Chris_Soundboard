from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your views here.

base = '/home/mellisor/django_servers/sound_django/'

def index(request):
    path = os.path.join(base,'static/home/Sounds/')
    bar_lst = os.listdir(path)
    cat_dct = dict()
    for cat in bar_lst:
        cat_path = os.path.join(path,cat)
        cat_dct[cat] = os.listdir(cat_path)
    if not request.user_agent.is_mobile:
        return render(request,'home/home.html',context={'cats':cat_dct})
    return render(request,'home/mobile.html',context={'cats':cat_dct})
