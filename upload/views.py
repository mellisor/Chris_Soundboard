from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
        return redirect(reverse('upload:index'))
    return render(request, 'upload/login.html')


def index(request):
    return render(request, 'upload/index.html')
