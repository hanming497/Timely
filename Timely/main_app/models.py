from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# super user is: han, han@han.com, han123HAN


class Timezones(models.Model):
    timezone = models.ForeignKey(
        'iana_timezones', on_delete=models.CASCADE, null=True)
    hour_toggle = models.BooleanField(default=False)
    availability_start_time = models.CharField(max_length=100, default='00:00')
    availability_end_time = models.CharField(max_length=100, default='23:59')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, default='Toronto')
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, null=True, default='Canada')
    name = models.CharField(max_length=100, default='Princeton')

    def __str__(self):
        return self.name + ' - ' + str(self.timezone) + ' - ' + str(self.city) + ' - ' + self.availability_start_time + ' - ' + self.availability_end_time + ' - ' + str(self.hour_toggle)


class iana_timezones(models.Model):
    iana_timezone = models.CharField(max_length=100)

    def __str__(self):
        return self.iana_timezone


class City(models.Model):

    city_name = models.CharField(max_length=100)

    def __str__(self):  # show the actual city name on the dashboard
        return self.city_name

    class Meta:  # show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'


class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_short_name = models.CharField(max_length=100)
    country_phone_code = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name
