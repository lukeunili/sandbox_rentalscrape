from django.shortcuts import render
from.forms import SearchInput

# Create your views here.


#def home_view(httprequest, *args):
 #   return render(httprequest, "home.html")

def QueryCreateView(httprequest, *args, **kwargs):
    search_form = SearchInput(httprequest.POST or None)
    #if search_form.is_valid():
    search_form.save()
    search_form = SearchInput()

    context = {
        "form": search_form
    }

    return render(httprequest, "home.html", context)