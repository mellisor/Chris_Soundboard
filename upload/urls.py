from django.urls import path
from . import views
app_name = "upload"

urlpatterns = [
    path('login', views.login, name="login"),
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('show_edit', views.show_edit, name="show_edit"),
    path('edit/<int:id>', views.edit, name="edit"),
]
