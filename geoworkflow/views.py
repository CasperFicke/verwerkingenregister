# geoworkflow/views.py

# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

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

# add bagregistratie
def add_bagregistratie(request):
  title = 'add bagregistratie'
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

# all bagregistraties
def bagregistraties(request):
  title = 'bagregistraties'
  bagregistraties = Bagregistratie.objects.all()
  context = {
    'title'           : title,
    'bagregistraties' : bagregistraties,
  }
  return render(request, 'geoworkflow/all_bagregistraties.html', context)
