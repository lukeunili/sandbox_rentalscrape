from django.db import models

# Create your models here.


class SearchInput(models.Model):
    Station = models.CharField(max_length=120)
    Pickupdate = models.DateField()
    Pickuptimestart = models.TimeField()
    Pickuptimeend = models.TimeField()
    Dropoffdate = models.DateField()
    Dropofftimestart = models.TimeField()
    Dropofftimeend = models.TimeField()
