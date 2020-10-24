from django import forms
from .models import SearchInput

"""Define a widget to be able to use the datePicker
 for better usability"""

class DateInput(forms.DateInput):
    input_type = 'date'


"""Define a widget to be able to use the timePicker
 for better usability"""

class TimeInput(forms.TimeInput):
    input_type = 'time'


"""Define search form and corresponding widgets that
 are displayed to the user"""

class SearchForm2(forms.ModelForm):
    class Meta:
        model = SearchInput
        fields = ['Station', 'Pickupdate', 'Pickuptimestart', 'Pickuptimeend', 'Dropoffdate', 'Dropofftimestart', 'Dropofftimeend']
        widgets = {
            'Pickupdate': DateInput,
            'Dropoffdate': DateInput,
            'Pickuptimestart': TimeInput,
            'Pickuptimeend': TimeInput,
            'Dropofftimestart': TimeInput,
            'Dropofftimeend': TimeInput

        }