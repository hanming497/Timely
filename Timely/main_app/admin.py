from django.contrib import admin

from .models import Timezones, City

admin.site.register(Timezones)
admin.site.register(City)
