# waarmerken/forms.py

# Django
from django import forms
#from django.forms import ModelForm, DateInput

# Local
from .models import Documentwaarmerking

# Documentwaarmerkingform
class DocumentwaarmerkingForm(forms.ModelForm):
  class Meta:
    model = Documentwaarmerking
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
