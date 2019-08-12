from django.shortcuts import render
from sounds.serializers import *
from sounds.models import *
from rest_framework import viewsets
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SoundByteViewSet(viewsets.ModelViewSet):

    queryset = SoundByte.objects.all()
    serializer_class = SoundByteSerializer
