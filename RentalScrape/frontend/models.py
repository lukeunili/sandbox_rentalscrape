from django.db import models
import datetime as dt
from django.core.exceptions import ValidationError

# Create your models here.

begin_time = models.TimeField(default=dt.time(00, 00))

def no_past(value):
    today = dt.date.today()
    if value < today:
        raise ValidationError('Pick-up date cannot be in the past.')

#def after_pickup(value):
#    pickup = SearchInput.Pickupdate
#    if value < pickup:
#        raise ValidationError('Drop-off date must be after pick-up date.')


class SearchInput(models.Model):
    Station = models.CharField(verbose_name='Rental station', max_length=120)
    Pickupdate = models.DateField(verbose_name="Pick-up Date", validators=[no_past])
    Pickuptimestart = models.TimeField(verbose_name="Earliest Pick-Up time")
    Pickuptimeend = models.TimeField(verbose_name="Latest Pick-Up time", help_text= "<br>Please be aware, that latest pick-up time should be <strong>no later than 2 hours</strong> after first pick-up time.")
    Dropoffdate = models.DateField(verbose_name="Drop-off Date")
    Dropofftimestart = models.TimeField(verbose_name="Earliest Drop-off time")
    Dropofftimeend = models.TimeField(verbose_name="Latest Drop-Off time", help_text= "<br>Please be aware, that latest drop-off time should be <strong>no later than 2 hours</strong> after first drop-off time.")


class OfferList(models.Model):
    id = models.AutoField(primary_key=True)
    car_type = models.CharField(max_length=50)
    price_per_day = models.CharField(max_length=10)
    mileage = models.CharField(max_length=50)
    pickupdate = models.DateField()
    pickuptime = models.TimeField()
    dropoffdate = models.DateField()
    dropofftime = models.TimeField()
    bookingclass = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'allresults'

OfferList.objects = OfferList.objects.using('resultsdatabase')


