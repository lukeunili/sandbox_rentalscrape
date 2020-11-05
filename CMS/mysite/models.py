from django.db import models

# Create your models here.


class SearchInput(models.Model):
    Station = models.CharField(verbose_name='Rental station', max_length=120)
    Pickupdate = models.DateField(verbose_name="Pick-up Date")
    Pickuptimestart = models.TimeField(verbose_name="Earliest Pick-Up time")
    Pickuptimeend = models.TimeField(verbose_name="Latest Pick-Up time")
    Dropoffdate = models.DateField(verbose_name="Drop-off Date")
    Dropofftimestart = models.TimeField(verbose_name="Earliest Drop-off time")
    Dropofftimeend = models.TimeField(verbose_name="Latest Drop-Off time")
