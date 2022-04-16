from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
from .models import *
from .forms import CityForm
import pendulum


from django.contrib.auth.forms import UserCreationForm
# Add the following import


# Define the home view


def home(request):
    return render(request, 'home.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()

            return redirect('/login')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def login(request):
    return render(request, 'registration/login.html')


@login_required
def timezones(request):
    timezones = Timezones.objects.filter(
        user=request.user)  # returns all timezones

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
    country_code = []
    start_data = []
    end_data = []
    sunrise_sundown_data = [100, 50]
    timezones_id = []

    for timezone in timezones:
        timezones_arr = str(timezone).split('-')
        name_data.append("".join(timezones_arr[0].split()))
        timezones_data.append("".join(timezones_arr[1].split()))
        city_data.append(timezones_arr[2])
        start_data.append("".join(timezones_arr[3].split()))
        end_data.append("".join(timezones_arr[4].split()))
        timezones_id.append(timezone.id)
        country_code.append(timezone.country.country_short_name)

    for i, city in enumerate(city_data):

        # request the API data and convert the JSON to Python data types
        city_weather = requests.get(url.format(city, country_code[i])).json()
        # print(city_weather)

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
            'id': timezones_id[i],
        }

        temperature_comparison = round(city_weather['main']['temp'])
        feels_like_comparison = round(city_weather['main']['feels_like'])

        if temperature_comparison == feels_like_comparison:
            data_object['feels_like'] = 'Feels similar'
        elif temperature_comparison > feels_like_comparison:
            data_object['feels_like'] = 'Feels cooler'
        elif temperature_comparison < feels_like_comparison:
            data_object['feels_like'] = 'Feels warmer'

        timezones_dto_data.append(data_object),

    # for sunrise and sundown progressbar
    # if timezones_data is not empty

    if timezones_data:
        city_weather = requests.get(url.format(city_data[0])).json()
        sr = pendulum.from_timestamp(
            city_weather['sys']['sunrise'], tz=timezones_data[0])

        sd = pendulum.from_timestamp(
            city_weather['sys']['sunset'], tz=timezones_data[0])

        curr = pendulum.now(timezones_data[0])
        total_diff = sd.diff(sr).in_hours()
        current_diff = sr.diff(curr).in_hours()
        sunrise_sundown_data[0] = total_diff
        sunrise_sundown_data[1] = current_diff

    # creating timezoneDTO

    timezoneDTO = {
        'timezones': timezones_dto_data,
        'sunrise_sundown': sunrise_sundown_data,

    }

    return render(request, 'timezones.html', timezoneDTO)


class TimezonesCreate(CreateView):
    model = Timezones
    fields = ['country', 'city', 'timezone',
              'availability_start_time', 'availability_end_time', 'name']
    success_url = '/timezones/'

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the timezone
        # Let the CreateView do its job as usual
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["country_list"] = Country.objects.all()
        return context


class TimezonesDelete(DeleteView):
    model = Timezones
    success_url = '/timezones/'


def timezones_detail(request, timezone_id):
    timezone = Timezones.objects.get(id=timezone_id)
    timezone_data = {
        'timezone': timezone,
    }
    return render(request, 'timezones_detail.html', timezone_data)
