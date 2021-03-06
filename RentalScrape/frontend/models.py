from django.db import models
import datetime as dt
from django.core.exceptions import ValidationError

# Create your models here.

def no_past(value):
    """Validation to ensure, users don't insert dates from the past"""
    today = dt.date.today()
    if value < today:
        raise ValidationError('Pick-up date cannot be in the past.')


class SearchInput(models.Model):
    """Model that serves as a basis for the form at /home. Users put in their search request,
    this search request is then processed in Scrape_sqlite.py for scraping. Some validators like
    "no_past" are used for form validation. All search requests can be seen in this model."""
    Station = models.CharField(verbose_name='Rental station', max_length=120)
    Pickupdate = models.DateField(verbose_name="Pick-up Date", validators=[no_past])
    Pickuptimestart = models.TimeField(verbose_name="Pick-Up time")
    Pickuptimeend = models.TimeField(verbose_name="Latest Pick-Up time", default="08:00:00", help_text= "<br>Please be aware, that latest pick-up time should be <strong>no later than 2 hours</strong> after first pick-up time.")
    Dropoffdate = models.DateField(verbose_name="Drop-off Date")
    Dropofftimestart = models.TimeField(verbose_name="Drop-off time")
    Dropofftimeend = models.TimeField(verbose_name="Latest Drop-Off time", default="08:00:00", help_text= "<br>Please be aware, that latest drop-off time should be <strong>no later than 2 hours</strong> after first drop-off time.")


class Offer(models.Model):
    """This model is used to save the scraped data and display it to the user at /results.
    In Scrape_sqlite.py the data is written directly into the sqlite table frontend_offer"""
    cartype = models.CharField(max_length=50, blank=True, null=True, default="")
    price = models.CharField(max_length=100, blank=True, null=True, default="")
    mileage = models.CharField(max_length=50, blank=True, null=True, default="")
    pickupdate = models.CharField(max_length=100, blank=True, null=True, default="")
    pickuptime = models.TimeField()
    pickuptimes = models.CharField(max_length=4, blank=True, null=True, default="")
    dropoffdate = models.CharField(max_length=100, blank=True, null=True, default="")
    dropofftime = models.TimeField()
    dropofftimes = models.CharField(max_length=4, blank=True, null=True, default="")
    bookingclass = models.CharField(max_length=4, blank=True, null=True, default="")
    cardescription = models.CharField(max_length=40, blank=True, null=True, default="")
    searchid = models.CharField(max_length=10, blank=True, null=True, default="")
    imgurl = models.CharField(max_length=100, blank=True, null=True, default="")
    pickupstationid = models.CharField(max_length=10, blank=True, null=True, default="")
    returnstationid = models.CharField(max_length=10, blank=True, null=True, default="")



