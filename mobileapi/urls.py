from django.urls import path
from . import views

app_name = 'mobileapi'

urlpatterns = [
    path('',views.index,name='index'),
]
