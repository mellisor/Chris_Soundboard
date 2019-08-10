from django.urls import path
from . import views
app_name = "upload"

urlpatterns = [
    path('login', views.login, name="login"),
    path('',views.index,name="index"),
]