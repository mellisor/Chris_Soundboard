from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    errors = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(reverse('upload:index'))
        else:
                errors['error'] = 'Incorrect username or password'
    return render(request, 'upload/login.html',context=errors)


@login_required
def index(request):
    return render(request, 'upload/index.html')
