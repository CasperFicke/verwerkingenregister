# contacts/forms.py

# django
from django import forms

# local
from .models import Contact

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = (
      'name', 'phone'
    )
    widgets = {
      'name' : forms.TextInput(attrs={'class': 'form-control'}),
      'phone': forms.TextInput(attrs={'class': 'form-control'})
    }