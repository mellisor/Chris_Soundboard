from django.urls import path
from . import views

app_name = "sounds"

urlpatterns = [
    path('', views.index, name="index"),
]