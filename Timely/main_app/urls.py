from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),
    path('timezones/', views.weather, name='weather'),
    path('timezones/create/', views.TimezonesCreate.as_view(),
         name='timezones_create'),
]
