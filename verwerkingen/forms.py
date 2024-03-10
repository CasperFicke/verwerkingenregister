# verwerkingen/forms.py

# Django
from django import forms
from django.forms import ModelForm, DateInput

# Local
from .models import Verwerking, Verwerkersovereenkomst

# Verwerkingform
class VerwerkingForm(forms.ModelForm):
  class Meta:
    model = Verwerking
    fields = '__all__'
    labels = {
      "naam": "Your Name",
      "doel": "Your Feedback",
      "bewaartermijn": "Your Rating"
      }
    error_messages = {
      "user_name": {
        "required": "Your name must not be empty!",
        "max_length": "Please enter a shorter name!"
      }
      }

# Verwerkersovereenkomst form
class VerwerkersovereenkomstForm(ModelForm):
  class Meta:
    model  = Verwerkersovereenkomst
    fields = ('naam', 'beschrijving', 'pdf', 'verwerker', 'vwo_start', 'vwo_end', 'verwerkingen', 'extern')
    labels  = {
      'naam'         : 'VWO naam',
      'beschrijving' : 'VWO beschrijving',
      'pdf'          : 'VWO document',
      'verwerker'    : 'Verwerker',
      'vwo_start'    : 'startdatum',
      'vwo_end'      : 'einddatum',
      'verwerkingen' : 'verwerkingen',
      'extern'       : 'externe partij',
    }
    widgets = {
      'naam'         : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'naam'}),
      'beschrijving' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'beschrijving'}),
      'pdf'          : forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'bestand'}),
      'verwerker'    : forms.Select(attrs={'class': 'form-select', 'placeholder': 'verwerker'}),
      'vwo_start'    : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
      'vwo_end'      : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
      'verwerkingen' : forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'verwerkingen'}),
      'extern'       : forms.CheckboxInput(attrs={}),
    }
