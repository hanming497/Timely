from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
from django.urls.base import reverse
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CityForm
import pendulum
# Add the following import


# Define the home view


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'registration/signup.html')


def login(request):
    return render(request, 'registration/login.html')


@login_required
def timezones(request):
    timezones = Timezones.objects.all() #returns all timezones 


    # Enter your API key here
    api_key = "ea43d349fe09f49a0d21b5607b77208c"

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + api_key

    

    if request.method == 'POST':  # only true if form is submitted
        # add actual request data to form for processing
        form = CityForm(request.POST)
        form.save()  # will validate and save if validate

    form = CityForm()

    timezones_dto_data = []

    timezones_data = []
    name_data = []
    city_data = []
    start_data = []
    end_data = []

    for timezone in timezones:
        timezones_arr = str(timezone).split('-')
        name_data.append("".join(timezones_arr[0].split()))
        timezones_data.append("".join(timezones_arr[1].split()))
        city_data.append(timezones_arr[2])
        start_data.append("".join(timezones_arr[3].split()))
        end_data.append("".join(timezones_arr[4].split()))

    for i,city in enumerate(city_data):

        # request the API data and convert the JSON to Python data types
        city_weather = requests.get(url.format(city)).json()

        data_object = {
            'city': city,
            'country': city_weather['sys']['country'],
            'temperature': city_weather['main']['temp'],
            'feels_like': '',
            'temperature_rounded': round(city_weather['main']['temp']),
            'description': city_weather['weather'][0]['main'],
            'time': (pendulum.now(timezones_data[i])).strftime("%H:%M"),
            'icon': city_weather['weather'][0]['icon'],
            'name': name_data[i],
            'start_time': start_data[i],
            'end_time': end_data[i],
        }
        
        temperature_comparison = round(city_weather['main']['temp'])
        feels_like_comparison = round(city_weather['main']['feels_like'])

        if temperature_comparison == feels_like_comparison:
            data_object['feels_like'] = 'Feels similar to ' + str(temperature_comparison)
        elif temperature_comparison > feels_like_comparison:
            data_object['feels_like'] =  'Feels cooler than ' + str(temperature_comparison)
        elif temperature_comparison < feels_like_comparison:
            data_object['feels_like'] = 'Feels warmer than '  + str(temperature_comparison)
        
        

        timezones_dto_data.append(data_object),
 

    timezoneDTO = {
        'timezones': timezones_dto_data,
    }

    return render(request, 'timezones.html', timezoneDTO)



class TimezonesCreate(CreateView):
    model = Timezones
    fields = ['timezone', 'availability_start_time', 'availability_end_time', 'name', 'city']
    success_url = '/timezones/'

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)









