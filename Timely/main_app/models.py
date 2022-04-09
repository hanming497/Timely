import pendulum
from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User


class Timezones(models.Model):
    timezone: models.CharField(max_length=150)
    user: models.ForeignKey(User, on_delete=models.CASCADE)
    hourToggle: models.BooleanField(default=False)
    availabilityStartTime: models.CharField(max_length=150, default='00:00')
    availabilityEndTime: models.CharField(max_length=150, default='23:59')

    def __str__(self):
        return self.timezone + ' - ' + self.availabilityStartTime + ' - ' + self.availabilityEndTime
    
