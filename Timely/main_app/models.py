from django.db import models
from django.urls import reverse
from datetime import date


class Timezones(models.Model):
    timezone= models.ForeignKey('iana_timezones', on_delete=models.CASCADE, null=True)
    hour_toggle= models.BooleanField(default=False)
    availability_start_time= models.CharField(max_length=100, default='00:00')
    availability_end_time= models.CharField(max_length=100, default='23:59')

    def __str__(self):
        return self.timezone + ' - ' + self.availabilityStartTime + ' - ' + self.availabilityEndTime

class iana_timezones(models.Model):
    iana_timezone= models.CharField(max_length=100)


    def __str__(self):
        return self.iana_timezone


