from django import forms
from .models import Event,Service



class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        labels = {"service_name" : "Usługa "}

class EventForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all(),label='Usługa ')
    date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}),label='Data ')
    time =  forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}),label='Godzina ')
    paid = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'style': 'width:1rem'}),label='Opłacono ')
    class Meta:
        model = Event
        fields = "__all__"
        labels = {
            'first_name' : 'Imie i nazwisko ',
            'number' : 'Numer telefonu ',
            'description' : 'Opis / notatka ',
        }