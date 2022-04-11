from django.shortcuts import render

from django.views.generic.edit import CreateView
from .models import Timezones
# Add the following import
from django.http import HttpResponse

# Define the home view


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')


def timezones(request):
    return render(request, 'timezones.html', {'timezones': timezones})

class TimezonesCreate(CreateView):
    model = Timezones
    fields = ['timezone', 'availability_start_time', 'availability_end_time']
    success_url = '/timezones/'