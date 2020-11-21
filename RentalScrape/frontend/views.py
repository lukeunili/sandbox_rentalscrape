from django.shortcuts import render, HttpResponse
from .forms import SearchForm2
from .models import Offer
from django.views.generic import ListView
import pandas as pd
import sqlite3
import os.path
from pandas import DataFrame as Results

# Create your views here.

#def home_view(httprequest, *args):
 #   return render(httprequest, "home.html")

def QueryCreateView(httprequest, *args, **kwargs):
    search_form = SearchForm2(httprequest.POST or None)
    if search_form.is_valid():
        search_form.save()
        search_form = SearchForm2()

    context = {
        "form": search_form,
    }

    return render(httprequest, "home.html", context)


def aboutus(httprequest):
    return render(httprequest, "aboutus.html")

def LoadingView(httprequest):
    return render(httprequest, "loading.html")

def tipstricks(httprequest):
    return render(httprequest, "tipstricks.html")

"""def OfferListResult(request):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "results.db")
    Connection = sqlite3.connect(db_path)
    Cursor = Connection.cursor()
    Cursor.execute("SELECT car_type, price_per_day, pickuptime, dropofftime, mileage FROM allresults ORDER BY price_per_day +0 asc")
    OffersList = Cursor.fetchall()
    Connection.close()
    return render(request, "results.html", {'OffersList': OffersList})"""


def OfferList(httprequest, *args, **kwargs):
    allOffers = Offer.objects.all()
    context = {
        "allOffers": allOffers,
        "title": "All offers",
        }

    return render(httprequest, "results.html", context)


#def OfferList(request):
#    conn = sql.connect('results.db')
#    results = pd.read_sql('SELECT * FROM allresults', conn)
    # 'tableview/static/csv/20_Startups.csv' is the django
    # directory where csv file exist.
    # Manipulate DataFrame using to_html() function
    #geeks_object = results.to_html()

    #return render(geeks_object, "results.html")


