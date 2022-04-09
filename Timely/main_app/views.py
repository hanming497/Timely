from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def timezones(request):
    return render(request, 'timezones.html', {'timezones': timezones})