from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class SoundByte(models.Model):

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.name