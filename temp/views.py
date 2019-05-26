from django.shortcuts import render
from subprocess import check_output
from django.http import HttpResponse
# Create your views here.

def index(request):
    temp = str(check_output(["sensors"]))
    return render(request,"temperature.html",context={'temp':temp})
