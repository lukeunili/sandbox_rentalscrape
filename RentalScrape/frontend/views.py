from django.shortcuts import render
from .forms import SearchForm2
from .models import Offer
from django.http import HttpResponseRedirect
from django.db.models import Count
from threading import *



# Create your views here.


def QueryCreateView(httprequest, *args, **kwargs):
    """View that displays SearchForm2 on /home and saves input to SearchInput model for further processing.
    If form is submitted, Scrape_sqlite.py is triggered and user is redirected to /results after execution of script."""
    search_form = SearchForm2(httprequest.POST or None)
    if search_form.is_valid():
        search_form.save()
        search_form = SearchForm2()
        from .Scrape_sqlite import Scrape
        t1 = Scrape()
        t1.start()
        return HttpResponseRedirect('results/')

    context = {
        "form": search_form,
    }

    return render(httprequest, "home.html", context)


def aboutus(httprequest):
    """This view returns aboutus.html to /aboutus"""
    return render(httprequest, "aboutus.html")


def tipstricks(httprequest):
    """This view returns tipstricks.html to /tipstricks"""
    return render(httprequest, "tipstricks.html")


def BookingclassView(httprequest, bc):
    """This view returns the results for each bookingclass"""

    bookingclassOffers = Offer.objects.all() \
        .values('bookingclass', 'price', 'cardescription', 'cartype', 'pickupdate', 'pickuptime', 'dropoffdate', 'dropofftime', 'mileage') \
        .filter(bookingclass=bc) \
        .order_by('price')

    context = {
        "bookingclassOffers": bookingclassOffers,
        "title": "bookingclassoffers",
    }
    return render(httprequest, "results_detail.html", context)


def OfferListBookingclass(httprequest, *args, **kwargs):
    """This view returns the result organized by bookingclass and price"""
    bookingclassOffers = Offer.objects.all()\
        .values('bookingclass', 'price', 'cardescription', 'cartype')\
        .annotate(dcount=Count('bookingclass'))\
        .order_by('price')
    context = {
        "bookingclassOffers": bookingclassOffers,
        "title": "bookingclassoffers",
    }

    return render(httprequest, "results_overview.html", context)


def OfferList(httprequest, *args, **kwargs):
    """This view renders the objects out of the offer model
    (meaning the scraped SIXT-rates) for the user to
    display at /results, orderer ascending by price"""

    allOffers = Offer.objects.all().order_by('price')
    context = {
        "allOffers": allOffers,
        "title": "All offers",
        }

    return render(httprequest, "results_legacy.html", context)








