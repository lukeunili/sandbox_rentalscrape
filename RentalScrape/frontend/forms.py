from django import forms
from .models import SearchInput


STATION_CHOICE = (
    ("Triesen", "Triesen"),
    ("Muenchen Flughafen", "Muenchen Flughafen"),
    ("Konstanz", "Konstanz"),
    ("Lindau", "Lindau"),
    ("Friedrichshafen", "Friedrichshafen"),
    ("Solln", "Solln"),
    ("Dornbirn", "Dornbirn"),
    ("Wien-Schwechat Flughafen", "Wien-Schwechat Flughafen")
)
"""List of available SIXT Stations"""


TIME_CHOICES_FIRST_HARD = (
    ("08:00", "08:00 - 10:00"),
    ("08:30", "08:30 - 10:30"),
    ("09:00", "09:00 - 11:00"),
    ("09:30", "09:30 - 11:30"),
    ("10:00", "10:00 - 12:00"),
    ("10:30", "10:30 - 12:30"),
    ("11:00", "11:00 - 13:00"),
    ("11:30", "11:30 - 13:30"),
    ("12:00", "12:00 - 14:00"),
    ("12:30", "12:30 - 14:30"),
    ("13:00", "13:00 - 15:00"),
    ("13:30", "13:30 - 15:30"),
    ("14:00", "14:00 - 16:00"),
    ("14:30", "14:30 - 16:30"),
    ("15:00", "15:00 - 17:00"),
    ("15:30", "15:30 - 17:30"),
    ("16:00", "16:00 - 18:00")
)
"""List of available Pick-Up times"""


TIME_CHOICES_LAST_HARD = (
    ("08:00", "08:00 - 10:00"),
    ("08:30", "08:30 - 10:30"),
    ("09:00", "09:00 - 11:00"),
    ("09:30", "09:30 - 11:30"),
    ("10:00", "10:00 - 12:00"),
    ("10:30", "10:30 - 12:30"),
    ("11:00", "11:00 - 13:00"),
    ("11:30", "11:30 - 13:30"),
    ("12:00", "12:00 - 14:00"),
    ("12:30", "12:30 - 14:30"),
    ("13:00", "13:00 - 15:00"),
    ("13:30", "13:30 - 15:30"),
    ("14:00", "14:00 - 16:00"),
    ("14:30", "14:30 - 16:30"),
    ("15:00", "15:00 - 17:00"),
    ("15:30", "15:30 - 17:30"),
    ("16:00", "16:00 - 18:00")
)
"""List of available Drop-Off times"""


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
            'Pickuptimeend': forms.HiddenInput,
            'Dropofftimestart': forms.Select(choices=TIME_CHOICES_FIRST_HARD),
            'Dropofftimeend': forms.HiddenInput,
        }