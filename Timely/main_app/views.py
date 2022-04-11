from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
import requests

from .models import Timezones
from .models import City

from main_app.forms import CityForm

# Add the following import


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


def weather(request):

    # Enter your API key here
    api_key = "ea43d349fe09f49a0d21b5607b77208c"

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + api_key

    cities = City.objects.all()  # return all the cities in the database

    if request.method == 'POST':  # only true if form is submitted
        # add actual request data to form for processing
        form = CityForm(request.POST)
        form.save()  # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:

        # request the API data and convert the JSON to Python data types
        city_weather = requests.get(url.format(city)).json()

        print(city_weather)

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        # add the data for the current city into our list
        weather_data.append(weather)

    context = {'weather_data': weather_data}

    return render(request, 'weather.html', context)
