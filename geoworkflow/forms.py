# geoworkflow/forms.py

# django
from django import forms
from django.forms import ModelForm, DateInput

from .models import Bagregistratie, Notitie

# BAGregistratie form
class BagregistratieForm(ModelForm):
  class Meta:
    model  = Bagregistratie
    fields = (
      'gemeente',
      'straat',
      'bagobjecttype',
      'baggebeurtenis', 
      'besluit', 'datum_besluit', 
      'datum_ontvangst',
      'volledig_ontvangen',
      'juist_aangeleverd',
      'tarief'
    )
    labels  = {
      'gemeente'           : 'Gemeente',
      'straat'             : 'straat',
      'bagobjecttype'      : 'bagobjecttype',
      'baggebeurtenis'     : 'baggebeurtenis',
      'besluit'            : 'besluit',
      'datum_besluit'      : 'datum besluit',
      'datum_ontvangst'    : 'datum ontvangst',
      'volledig_ontvangen' : 'volledig ontvangen',
      'juist_aangeleverd'  : 'juist aangeleverd',
      'tarief'             : 'tarief'
    }
    widgets = {
      'gemeente'           : forms.TextInput(attrs={'class': 'form-control'}),
      'straat'             : forms.TextInput(attrs={'class': 'form-control'}),
      'bagobjecttype'      : forms.TextInput(attrs={'class': 'form-control'}),
      'baggebeurtenis'     : forms.TextInput(attrs={'class': 'form-control'}),
      'besluit'            : forms.TextInput(attrs={'class': 'form-control'}),
      'datum_besluit'      : DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
      'datum_ontvangst'    : DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
      #'volledig_ontvangen' : forms.CheckboxInput(),
      #'juist_aangeleverd'  : forms.CheckboxInput(),
      #'tarief'             : forms.Select(attrs={'class': 'form-control'}) 
    }

# Notitie form
class NotitieForm(forms.ModelForm):
  class Meta:
    model = Notitie
    fields = (
      'title',
      'body'
    )
    widgets = {
      'title' : forms.TextInput(attrs={'class': 'form-control'}),
      'body'  : forms.TextInput(attrs={'class': 'form-control'})
    }
