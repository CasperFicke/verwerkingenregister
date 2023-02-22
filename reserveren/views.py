# reserveren/views.py

# django
from django.http import HttpResponse
from django.shortcuts import render

from formtools.wizard.views import SessionWizardView

# local
from .forms import GuestDetailForm, BusinessDetailForm, BookingDetailForm

# determen is 2e form should be displayed
def show_business_form(wizard):
  cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
  return cleaned_data.get('is_business_guest')

# reserveren view
class BookingWizardView(SessionWizardView):
  form_list      = [GuestDetailForm, BusinessDetailForm, BookingDetailForm]
  template_name  = 'reserveren/maak_reservering.html'
  condition_dict = {'1': show_business_form}

  def done(self, form_list, **kwargs):
    guest_form = form_list[0]
    if guest_form.cleaned_data.get('is_business_guest'):
      business       = form_list[1].save()
      guest          = guest_form.save(commit=False)
      guest.business = business
      guest.save()
    else:
      guest = guest_form.save()
    booking = form_list[-1].save(commit=False)
    booking.guest = guest
    booking.save()

    return HttpResponse("form submitted")
    #return render(self.request, 'done.html', {
    #  'form_data': [form.cleaned_data for form in form_list],
    #})