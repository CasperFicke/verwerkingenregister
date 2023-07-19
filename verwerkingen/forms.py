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
    fields = ('naam', 'beschrijving', 'verwerker', 'vwo_start', 'vwo_end', 'extern')
    labels  = {
      'naam'         : 'VWO naam',
      'beschrijving' : 'VWO beschrijving',
      'verwerker'    : 'Verwerker',
      'vwo_start'    : 'startdatum',
      'vwo_end'      : 'einddatum',
      'extern'       : 'externe partij',
    }
    widgets = {
      'naam'         : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'naam'}),
      'beschrijving' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'beschrijving'}),
      'verwerker'    : forms.Select(attrs={'class': 'form-select', 'placeholder': 'verwerker'}),
      #'vwo_start'    : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'startdatum'}),
      #'vwo_end'      : forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'einddatum'}),
      'vwo_start'    : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
      'vwo_end'      : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
    }
