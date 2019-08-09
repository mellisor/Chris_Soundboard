from django.db import models
from django.conf import settings
import os
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

def upload_file_path(instance,filename):
    print(filename)
    return 'sounds/{}/{}'.format(instance.category.name,filename.split('/')[-1].replace('_',' '))

class SoundByte(models.Model):

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_file_path,null=True)

    def __str__(self):
        return self.name