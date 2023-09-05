# geoworkflow/forms.py

# django
from django import forms

# local
from .models import Bagregistratie

# BAGregistratie detailform
class BagregistratieDetailForm(forms.ModelForm):
  class Meta:
    model   = Bagregistratie
    fields  = ('besluit', 'datum_besluit', 'datum_ontvangst', 'volledig_ontvangen')
    widgets = {'date': forms.DateInput(attrs = {'type': 'date'})}
