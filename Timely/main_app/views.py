from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
import requests
from django.urls.base import reverse
from .models import Timezones
from .models import City
from .forms import CityForm

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
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)

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
    feels_like_data = []

    for city in cities:

        # request the API data and convert the JSON to Python data types
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city': city,
            # 'country': city_weather['sys'][0]['country'],
            'temperature': city_weather['main']['temp'],
            'feels_like': round(city_weather['main']['feels_like']),
            'temperature_rounded': round(city_weather['main']['temp']),
            'description': city_weather['weather'][0]['main'],
            'icon': city_weather['weather'][0]['icon']
        }

        """
        temperature_comparison = round(city_weather['main']['temp'])
        feels_like_comparison = round(city_weather['main']['feels_like'])

        feels_like = {
            'Feels cooler': temperature_comparison > feels_like_comparison,
            'Feels warmer': temperature_comparison < feels_like_comparison,
            'Feels similar': temperature_comparison == feels_like_comparison
        }

        print(feels_like)

        if temperature_comparison == feels_like_comparison:
            feels_like_data.append('Feels similar')
        elif temperature_comparison > feels_like_comparison:
            feels_like_data.append('Feels cooler')
        elif temperature_comparison < feels_like_comparison:
            feels_like_data.append('Feels warmer').join(map(str, s))


        feels_like = {
            'Feels cooler': 'temperature_rounded' > 'feels_like',
            'Feels warmer': 'temperature_rounded' < 'feels_like',
            'Feels similar': 'temperature_rounded' == 'feels_like'
        }

        print(feels_like)
        print(weather)
        """

    # add the data for the current city into our list
        weather_data.append(weather),
        # feels_like_data.append(feels_like)

    context = {
        'weather_data': weather_data,
        'feels_like': feels_like_data
    }

    return render(request, 'timezones.html', context)
