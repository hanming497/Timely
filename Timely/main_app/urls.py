from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('timezones/', views.timezones, name='timezones'),
    path('timezones/<int:timezone_id>/', views.timezones_detail, name='detail'),
    path('timezones/create/', views.TimezonesCreate.as_view(), name='timezones_create'),
    # path('timezones/<int:pk>/update/', views.TimezonesUpdate.as_view(), name='timezones_update'),
    path('timezones/<int:pk>/delete/', views.TimezonesDelete.as_view(), name='timezones_delete'),
]
