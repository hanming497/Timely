from django.db import models
from django.urls import reverse
from datetime import date


class Timezones(models.Model):
    timezone = models.CharField(max_length=100)
    hour_toggle = models.BooleanField(default=False)
    availability_start_time = models.CharField(max_length=100, default='00:00')
    availability_end_time = models.CharField(max_length=100, default='23:59')

    # def __str__(self):
    #     return self.timezone + ' - ' + self.availabilityStartTime + ' - ' + self.availabilityEndTime


class City(models.Model):

    city_name = models.CharField(max_length=25)

    def __str__(self):  # show the actual city name on the dashboard
        return self.city_name

    class Meta:  # show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'
