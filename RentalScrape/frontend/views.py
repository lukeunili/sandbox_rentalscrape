from django.shortcuts import render
from .forms import SearchForm2
from .models import Offer


# Create your views here.


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


def OfferList(httprequest, *args, **kwargs):
    allOffers = Offer.objects.all()
    context = {
        "allOffers": allOffers,
        "title": "All offers",
        }

    return render(httprequest, "results.html", context)

