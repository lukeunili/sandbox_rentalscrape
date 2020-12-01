from django.shortcuts import render, redirect
from .forms import SearchForm2
from .models import Offer



# Create your views here.


def QueryCreateView(httprequest, *args, **kwargs):
    """View that displays SearchForm2 on /home and saves input
    to SearchInput model for further processing.
    In the future, this view should redirect to /loading and
    trigger Scrape_sqlite.py after POST"""
    search_form = SearchForm2(httprequest.POST or None)
    if search_form.is_valid():
        search_form.save()
        search_form = SearchForm2()
        from .Scrape_sqlite import Scrape
        Scrape()
        return redirect('/loading/')


    context = {
        "form": search_form,
    }


    return render(httprequest, "home.html", context)




def aboutus(httprequest):
    """This view returns aboutus.html to /aboutus"""
    return render(httprequest, "aboutus.html")

def LoadingView(httprequest):
    """This view returns loading.html to /loading.
    It should be triggered by the user submitting the /home form
    and should show as long as Scrape_sqlite.py is running.
    Once Scrape_sqlite.py finishes successfully, it should redirect to /results."""
    return render(httprequest, "loading.html")

def tipstricks(httprequest):
    """This view returns tipstricks.html to /tipstricks"""
    return render(httprequest, "tipstricks.html")


def OfferList(httprequest, *args, **kwargs):
    """This view renders the objects out of the offer model
    (meaning the scraped SIXT-rates) for the user to
    display at /results"""
    allOffers = Offer.objects.all().order_by('bookingclass', 'price')
    context = {
        "allOffers": allOffers,
        "title": "All offers",
        }

    return render(httprequest, "results.html", context)









