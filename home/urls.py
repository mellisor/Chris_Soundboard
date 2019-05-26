from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import urls as auth_urls

from . import views

app_name = "home"
urlpatterns = [
    path('accounts/',include(auth_urls)),
    path('', views.index, name="index"),
] 