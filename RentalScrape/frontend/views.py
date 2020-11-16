from django.shortcuts import render, HttpResponse
from .forms import SearchForm2
import pandas as pd
import sqlite3 as sql
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

def tipstricks(httprequest):
    return render(httprequest, "tipstricks.html")

#def OfferList(httprequest, *args, **kwargs):
#    allOffers = Results()
#    context = {
#        "allOffers": allOffers,
#        "title": "All offers"
#    }
#
#    return render(httprequest, "results.html", context)


# def OfferList(request):
#     conn = sql.connect('results.db')
#    results = pd.read_sql('SELECT * FROM allresults', conn)
#    # 'tableview/static/csv/20_Startups.csv' is the django
#    # directory where csv file exist.
#    # Manipulate DataFrame using to_html() function
#    geeks_object = results.to_html()

#    return render(geeks_object, "results.html")


