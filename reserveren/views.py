# reserveren/views.py

# django
from django.http import HttpResponse
from django.shortcuts import render

from formtools.wizard.views import SessionWizardView # form with multiple pages
from formtools.preview import FormPreview # form preview

# local
from .models import Guest
from .forms import GuestDetailForm, BusinessDetailForm, BookingDetailForm

# determen if 2e form should be displayed
def show_business_form(wizard):
  cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
  return cleaned_data.get('is_business_guest')

# reserveren view
class BookingWizardView(SessionWizardView):
  form_list      = [GuestDetailForm, BusinessDetailForm, BookingDetailForm]
  template_name  = 'reserveren/maak_reservering.html'
  condition_dict = {'1': show_business_form}
  def get_context_data(self,*args, **kwargs):
    context = super(BookingWizardView, self).get_context_data(*args,**kwargs)
    context['title'] = 'multiform'
    return context
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

#################
# form input with preview page
################

# form view
class GuestFormPreview(FormPreview):
  form_template    = 'reserveren/form_preview.html'
  preview_template = 'reserveren/preview_preview.html'
  def get_context_data(self,*args, **kwargs):
    context = super(GuestFormPreview, self).get_context_data(*args,**kwargs)
    context['title'] = 'preview form'
    return context
  def done(self, request, cleaned_data):
    Guest.objects.create(**cleaned_data)
    return HttpResponse('Form submitted')