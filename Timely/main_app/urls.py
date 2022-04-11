from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),
    path('timezones/', views.timezones, name='timezones'),
    path('weather/', views.weather, name='weather'),
]
