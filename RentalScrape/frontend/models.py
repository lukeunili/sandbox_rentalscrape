from django.db import models
import datetime as dt

# Create your models here.

begin_time = models.TimeField(default=dt.time(00, 00))


class SearchInput(models.Model):
    Station = models.CharField(verbose_name='Rental station', max_length=120)
    Pickupdate = models.DateField(verbose_name="Pick-up Date")
    Pickuptimestart = models.TimeField(verbose_name="Earliest Pick-Up time")
    Pickuptimeend = models.TimeField(verbose_name="Latest Pick-Up time", help_text= "<br>Please be aware, that latest pick-up time should be <strong>no later than 2 hours</strong> after first pick-up time.")
    Dropoffdate = models.DateField(verbose_name="Drop-off Date")
    Dropofftimestart = models.TimeField(verbose_name="Earliest Drop-off time")
    Dropofftimeend = models.TimeField(verbose_name="Latest Drop-Off time", help_text= "<br>Please be aware, that latest drop-off time should be <strong>no later than 2 hours</strong> after first drop-off time.")
