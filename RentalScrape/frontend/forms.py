from django import forms
from .models import SearchInput
import datetime as dt
from django.core.exceptions import ValidationError

"""Limit the choice of time in accordance with most sixt stations"""

TIME_CHOICES_FIRST = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(8, 19)] + [(dt.time(hour=x), '{:02d}:30'.format(x)) for x in range(8, 18)]
TIME_CHOICES_LAST = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(9, 21)] + [(dt.time(hour=x), '{:02d}:30'.format(x)) for x in range(8, 20)]

TIME_CHOICES_FIRST.sort()
TIME_CHOICES_LAST.sort()

"""Define a widget to be able to use the timePicker
 for better usability"""

class TimeInput(forms.TimeInput):
    input_type = 'time'


"""Define a widget to be able to use the datePicker
 for better usability"""

class DateInput(forms.DateInput):
    input_type = 'date'


"""Define search form and corresponding widgets that
 are displayed to the user incl. limited times available for choice"""

class SearchForm2(forms.ModelForm):
    class Meta:
        model = SearchInput
        fields = ['Station', 'Pickupdate', 'Pickuptimestart', 'Pickuptimeend', 'Dropoffdate', 'Dropofftimestart', 'Dropofftimeend']
        widgets = {
            'Pickupdate': DateInput,
            'Dropoffdate': DateInput,
            'Pickuptimestart': forms.Select(choices=TIME_CHOICES_FIRST),
            'Pickuptimeend': forms.Select(choices=TIME_CHOICES_LAST),
            'Dropofftimestart': forms.Select(choices=TIME_CHOICES_FIRST),
            'Dropofftimeend': forms.Select(choices=TIME_CHOICES_LAST),

        }