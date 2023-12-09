from django import forms
from .models import Listing, Appointment


class ListingForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'mileage','color', 
                  'description', 'engine', 'transmisson', 'image'}


class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=15)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    services = forms.MultipleChoiceField(
        choices=[('oil', 'Oil Change'), ('lube', 'Lube / Filters')],
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Appointment
        fields = ['name', 'contact', 'date', 'services']  