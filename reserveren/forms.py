# reserveren/forms.py

# django
from django import forms

# local
from .models import Guest, Business, Booking

# Guest detailform
class GuestDetailForm(forms.ModelForm):
  BOOL_CHOICES      = [(True, 'Ja'), (False, 'Nee')]
  is_business_guest = forms.BooleanField(
    widget   = forms.RadioSelect(choices = BOOL_CHOICES),
    required = False
  )
  class Meta:
    model  = Guest
    fields = ('first_name', 'last_name', 'email', 'phone')

# Business detailform
class BusinessDetailForm(forms.ModelForm):
  class Meta:
    model  = Business
    fields = ('name',)

# Booking detailform
class BookingDetailForm(forms.ModelForm):
  class Meta:
    model   = Booking
    fields  = ('room_type', 'date', 'number_of_nights')
    widgets = {'date': forms.DateInput(attrs = {'type': 'date'})}

###############
# previeuw form
###############

# Guest form
class GuestForm(forms.ModelForm):

  class Meta:
    model  = Guest
    fields = ('first_name', 'last_name', 'email', 'phone')