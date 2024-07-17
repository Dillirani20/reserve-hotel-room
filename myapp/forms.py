# forms.py

from django import forms

class HotelSearchForm(forms.Form):
    location = forms.CharField(max_length=255, required=False, label='Search by Location')
