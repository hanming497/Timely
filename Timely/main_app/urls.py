from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('timezones/', views.timezones, name='timezones'),
    path('timezones/create/', views.TimezonesCreate.as_view(), name='timezones_create'),
]
