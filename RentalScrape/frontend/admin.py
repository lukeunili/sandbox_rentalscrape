from django.contrib import admin

# Register your models here.
from .models import SearchInput, OfferList

admin.site.register(SearchInput)
admin.site.register(OfferList)
