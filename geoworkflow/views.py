# geoworkflow/views.py

# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.http import Http404
from django.core.paginator import Paginator

from formtools.wizard.views import SessionWizardView # form with multiple pages

# local
from .models import Gemeente, Straat, Baggebeurtenis, Bagobjecttype, Bagregistratie
#from .forms import VerwerkingForm

# index view
class indexView(TemplateView):
	"""
    Geoworkflow index page.

    **Template:**

    :template:`geoworkflow/index.html`
    """
	template_name = "geoworkflow/index.html"

# all bagregistraties
def bagregistraties(request):
  title = 'bagregistraties'
  bagregistraties = Bagregistratie.objects.all()
  context = {
    'title'           : title,
    'bagregistraties' : bagregistraties,
  }
  return render(request, 'geoworkflow/all_bagregistraties.html', context)

# show bagregistratie
def show_bagregistratie(request, bagregistratie_id):
  try:
    bagregistratie = Bagregistratie.objects.get(id=bagregistratie_id)
    title    = 'bagregistratie: ' + bagregistratie.besluit
    context  = {
      'title'          : title,
      'bagregistratie' : bagregistratie,
    }
    return render(request, 'geoworkflow/show_bagregistratie.html', context)
  except:
    raise Http404()

# add bagregistratie
def add_bagregistratie(request):
  title          = 'add bagregistratie'
  bagobjecttypen = Bagobjecttype.objects.all()
  gemeenten      = Gemeente.objects.all()
  context = {
    'title'          : title,
    'gemeenten'      : gemeenten,
    'bagobjecttypen' : bagobjecttypen,
  }
  return render(request, 'geoworkflow/add_bagregistratie.html', context)

# straten
def straten(request):
  gemeente = request.GET.get('gemeente')
  straten  = Straat.objects.filter(gemeente=gemeente)
  context  = {
    'straten': straten
  }
  return render(request, 'geoworkflow/partials/straten.html', context)

# bag gebeurtenissen
def baggebeurtenissen(request):
  bagobjecttype     = request.GET.get('bagobjecttype')
  baggebeurtenissen = Baggebeurtenis.objects.filter(bagobjecttype=bagobjecttype)
  context = {
    'baggebeurtenissen': baggebeurtenissen
  }
  return render(request, 'geoworkflow/partials/baggebeurtenissen.html', context)
