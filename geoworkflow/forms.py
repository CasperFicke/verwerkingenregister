# geoworkflow/forms.py

# django
from django import forms
from django.forms import ModelForm, DateInput

from .models import Bagregistratie

# BAGregistratie form
class BagregistratieForm(ModelForm):
  class Meta:
    model  = Bagregistratie
    fields = ('gemeente', 'straat', 'bagobjecttype', 'baggebeurtenis', 'besluit', 'datum_besluit', 'datum_ontvangst')
    labels  = {
      'gemeente'        : 'Gemeente',
      'straat'          : 'straat',
      'bagobjecttype'   : 'bagobjecttype',
      'baggebeurtenis'  : 'baggebeurtenis',
      'besluit'         : 'besluit',
      'datum_besluit'   :'datum besluit',
      'datum_ontvangst' : 'datum ontvangst'
    }
    widgets = {
      'gemeente'        : forms.TextInput(attrs={'class': 'form-control'}),
      'straat'          : forms.TextInput(attrs={'class': 'form-control'}),
      'bagobjecttype'   : forms.TextInput(attrs={'class': 'form-control'}),
      'baggebeurtenis'  : forms.TextInput(attrs={'class': 'form-control'}),
      'besluit'         : forms.TextInput(attrs={'class': 'form-control'}),
      'datum_besluit'   : DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
      'datum_ontvangst' : DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
    }
