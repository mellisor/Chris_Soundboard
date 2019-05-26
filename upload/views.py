from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect  
from django.views.decorators.http import require_GET, require_POST
import os
# Create your views here.

base = '/home/mellisor/django_servers/sound_django/static/home/Sounds/'

def index(request):
    return render(request,"upload/index.html")

def create(request):
    # Check for post request
    if request.method == 'POST':
        form = request.POST
        # Get posted file
        f = request.FILES['file']
        fname = f.name
        # If the file is not a wav file, redirect to create
        if fname[-4:] != '.wav':
            path = os.path.join(base)
            bar_lst = os.listdir(path)
            return render(request,"upload/create.html",context={'dirs':bar_lst,'form':form})
        # Get dirname to create file in
        dirname = request.POST['cats']
        # If you plan to create a new directory
        if dirname == 'New':
            # Change dirname to entered one
            dirname = request.POST['NewName']
            dirname = dirname.upper()
            # Make sure the user isn't trying to create a directory below the desired root
            if '..' in dirname:
                return HttpResponseRedirect('/upload')
            makeDir(request,dirname,fname)
        # Handle Posted File
        with open(base + dirname + '/' + fname,'wb+') as f:
            f.write(request.FILES['file'].read())
        return HttpResponseRedirect('/upload')
    # This is for the GET request, return all the subdirectories in Sounds
    path = os.path.join(base)
    bar_lst = os.listdir(path)    
    return render(request,"upload/create.html",context={'dirs':bar_lst})

def makeDir(request,dirname,fname):
    # Makes a directory if it doesn't already exist
    if not os.path.exists(base + dirname):
        os.makedirs(base + dirname)

def delete(request):
    # For post request
    if request.method == 'POST':
        # Get path to delete
        pth = base + request.POST['item']
        # Make sure you're not deleting anything below desired root
        if os.path.exists(pth) and '..' not in pth:
            os.remove(pth)
            checkDir(pth)
        return HttpResponseRedirect('/upload')
    # For get request, return all elements in directories
    dirs = {k:os.listdir(base + k) for k in os.listdir(base)}
    return render(request,"upload/delete.html",context={'cats':dirs})

def checkDir(pth):
    # See if there are any sounds remaining in directory. If not, delete
    baseDir = "/".join(pth.split("/")[:-1])
    if len(os.listdir(baseDir)) == 0:
        os.removedirs(baseDir)