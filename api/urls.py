from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'categories',views.CategoryViewSet)
router.register(r'soundbytes',views.SoundByteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
