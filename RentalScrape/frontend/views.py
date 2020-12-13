from django.shortcuts import render
from .forms import SearchForm2
from .models import Offer
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.db.models import Min
from time import sleep

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
        #from .Scrape_DE import ScrapeDE



        t1 = Scrape()
        #t2 = ScrapeDE()

        t1.start()
        #sleep(0.2)
        #t2.start()

        return HttpResponseRedirect('results/')

    context = {
        "form": search_form,
    }

    return render(httprequest, "home.html", context)


def LoadingView(httprequest):
    """ ---- INACTIVE ----
    This view returns loading.html to /loading.
    It should be triggered by the user submitting the /home form
    and should show as long as Scrape_sqlite.py is running.
    Once Scrape_sqlite.py finishes successfully, it should redirect to /results."""

    return render(httprequest, "loading.html")

def aboutus(httprequest):
    """This view returns aboutus.html to /aboutus"""
    return render(httprequest, "aboutus.html")


def tipstricks(httprequest):
    """This view returns tipstricks.html to /tipstricks"""
    return render(httprequest, "tipstricks.html")

def BookingclassView(httprequest, pk):
    """This view returns the resultpage for each bookingclass"""
    bookingclassallOffers = Offer.objects.all() \
        .values('bookingclass', 'price', 'cardescription', 'cartype') \
        .annotate(dcount=Count('bookingclass')) \
        .order_by('price')
    context = {
        "bookingclassOffers": bookingclassallOffers,
        "title": "bookingclassoffers",
    }
    return render(httprequest, "bookingclass.html")


def OfferListBookingclass(httprequest, *args, **kwargs):
    bookingclassOffers = Offer.objects.all()\
        .values('bookingclass', 'price', 'cardescription', 'cartype')\
        .annotate(dcount=Count('bookingclass'))\
        .order_by('price')
    context = {
        "bookingclassOffers": bookingclassOffers,
        "title": "bookingclassoffers",
    }

    return render(httprequest, "resultsbookingclass.html", context)

def OfferList(httprequest, *args, **kwargs):
    """This view renders the objects out of the offer model
    (meaning the scraped SIXT-rates) for the user to
    display at /results, orderer ascending by price"""




    allOffers = Offer.objects.all().order_by('price')
    context = {
        "allOffers": allOffers,
        "title": "All offers",
        }

    return render(httprequest, "results.html", context)








