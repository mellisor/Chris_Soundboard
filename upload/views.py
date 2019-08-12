from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from sounds.forms import CategoryForm, SoundByteForm
from sounds.models import Category, SoundByte
import json, os
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
    return render(request, 'upload/login.html', context=errors)


@login_required
def index(request):
    return render(request, 'upload/index.html')


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'category':
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                return render(request, 'upload/create.html', context={
                    'category_form': CategoryForm(), 'soundbyte_form': SoundByteForm(), 'category_create': True})
            else:
                return render(request, 'upload/create.html', context={'category_form': category_form, 'soundbyte_form': SoundByteForm()})
        elif request.POST.get('action') == 'soundbyte':
            soundbyte_form = SoundByteForm(request.POST, request.FILES)
            if soundbyte_form.is_valid():
                soundbyte_form.save()
                return render(request, 'upload/create.html', context={'category_form': CategoryForm(), 'soundbyte_form': SoundByteForm(), 'soundbyte_create': True})
            else:
                return render(request, 'upload/create.html', context={'category_form': CategoryForm(), 'soundbyte_form': soundbyte_form})
    return render(request, 'upload/create.html', context={'category_form': CategoryForm(), 'soundbyte_form': SoundByteForm})


@login_required
def show_edit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sound = SoundByte.objects.get(id=data['id'])
        if data.get('deleteFile') and sound.file:
            os.remove(sound.file.path)
        sound.delete()
        return HttpResponse()
    categories = Category.objects.all()
    return render(request, 'upload/show_edit.html', context={'categories': categories})

@login_required
def edit(request,id):
    if request.method == "POST":
        edit_form = SoundByteForm(request.POST,request.FILES,instance=SoundByte.objects.get(id=id))
        if edit_form.is_valid():
            edit_form.save()
            return render(request,'upload/edit.html',context={'edit_form':edit_form,'edit_success':True})
        return render(request,'upload/edit.html',context={'edit_form':edit_form,'edit_error':True})
    edit_form = SoundByteForm(instance=SoundByte.objects.get(id=id))
    return render(request,'upload/edit.html',context={'edit_form':edit_form})