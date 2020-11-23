from django import forms
from .models import SearchInput
import datetime as dt
from django.core.exceptions import ValidationError


STATION_CHOICE = (
    ("Muenchen Flughafen", "Muenchen Flughafen"),
    ("Wien-Schwechat Flughafen", "Wien-Schwechat Flughafen")
)
"""Generating list of available SIXT Stations"""


TIME_CHOICES_FIRST = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(8, 19)] + [(dt.time(hour=x), '{:02d}:30'.format(x)) for x in range(8, 18)]
TIME_CHOICES_LAST = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(9, 21)] + [(dt.time(hour=x), '{:02d}:30'.format(x)) for x in range(8, 20)]
"""Generating the Time Choices that will be shown in the Drop-Down list for pickup- and dropofftimes"""

TIME_CHOICES_FIRST_HARD = (
    ("08:00", "08:00 - 10:00"),
    ("08:30", "08:30 - 10:30")
)

TIME_CHOICES_FIRST.sort()
TIME_CHOICES_LAST.sort()
"""Sorting the Time Choices in the right order, e.g. 08:00, 08:30, 09:00, .."""


class TimeInput(forms.TimeInput):
    """Widget to be able to use the timePicker for better usability"""
    input_type = 'time'


class DateInput(forms.DateInput):
    """Widget to be able to use the datePicker for better usability"""
    input_type = 'date'


class SearchForm2(forms.ModelForm):
    """Define search form and corresponding widgets that
     are displayed to the user incl. limited times available for choice"""
    class Meta:
        model = SearchInput
        fields = ['Station', 'Pickupdate', 'Pickuptimestart', 'Pickuptimeend', 'Dropoffdate', 'Dropofftimestart', 'Dropofftimeend']
        widgets = {
            'Station': forms.Select(choices=STATION_CHOICE),
            'Pickupdate': DateInput,
            'Dropoffdate': DateInput,
            'Pickuptimestart': forms.Select(choices=TIME_CHOICES_FIRST_HARD),
            'Pickuptimeend': forms.Select(choices=TIME_CHOICES_LAST),
            'Dropofftimestart': forms.Select(choices=TIME_CHOICES_FIRST_HARD),
            'Dropofftimeend': forms.Select(choices=TIME_CHOICES_LAST),
        }