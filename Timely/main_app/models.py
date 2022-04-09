from django.db import models
from django.urls import reverse
from datetime import date


class Timezones(models.Model):
    timezone= models.CharField(max_length=100)
    hour_toggle= models.BooleanField(default=False)
    availability_start_time= models.CharField(max_length=100, default='00:00')
    availability_end_time= models.CharField(max_length=100, default='23:59')

    # def __str__(self):
    #     return self.timezone + ' - ' + self.availabilityStartTime + ' - ' + self.availabilityEndTime
