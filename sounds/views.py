from django.shortcuts import render
from .models import Category

# Create your views here.

def index(request):
    return render(request,"sounds/index.html",context={'categories':Category.objects.all()})