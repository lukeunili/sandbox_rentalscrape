from django.contrib import admin

# Register your models here.
from .models import SearchInput, Offer

admin.site.register(SearchInput)
admin.site.register(Offer)
