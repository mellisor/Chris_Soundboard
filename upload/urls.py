from django.urls import path, include
from . import views

app_name = 'upload'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('delete', views.delete, name='delete'),
]