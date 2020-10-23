from django import forms
from .models import SearchInput


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = SearchInput
        fields = ['Station', 'Pickupdate', 'Pickuptimestart', 'Pickuptimeend', 'Dropoffdate', 'Dropofftimestart', 'Dropofftimeend']

    def clean_station(self, *args, **kwargs):
        tmp = self.cleaned_data.get('Station')
        if len(tmp) < 10:
            raise forms.ValidationError("Station not available")
        return tmp
