from django.db import models
from django.contrib.auth.models import AbstractUser,User
from datetime import datetime

# Create your models here.


class User(AbstractUser):

    is_customer = models.BooleanField('Is customer', default=False)
    is_host = models.BooleanField('Is host', default=False)

    def __str__(self):
        return self.username

class DateModel(models.Model):
    user=models.ForeignKey(User, related_name='customer', verbose_name='Uname',on_delete=models.CASCADE,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    location = models.CharField(max_length=100,null=True)
    is_car = models.BooleanField('Car', default=False)
    is_bike = models.BooleanField('Bike', default=False)

    def __str__(self):
        return str(self.user)
