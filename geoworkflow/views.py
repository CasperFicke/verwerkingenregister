# geoworkflow/views.py

# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator

from formtools.wizard.views import SessionWizardView # form with multiple pages

# local
from .models import Gemeente, Straat, Baggebeurtenis, Bagobjecttype, Bagregistratie, Notitie
from .forms import BagregistratieForm, NotitieForm

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
  bagregistraties = Bagregistratie.objects.all().order_by('gemeente', '-datum_besluit')
  context = {
    'title'           : title,
    'bagregistraties' : bagregistraties,
  }
  return render(request, 'geoworkflow/all_bagregistraties.html', context)

# show bagregistratie
def show_bagregistratie(request, bagregistratie_id):
  try:
    bagregistratie = Bagregistratie.objects.get(id=bagregistratie_id)
    print(bagregistratie)
    #title    = 'bagregistratie: ' + bagregistratie.besluit
    context  = {
      #'title'          : title,
      'bagregistratie' : bagregistratie,
    }
    return render(request, 'geoworkflow/show_bagregistratie.html', context)
  except:
    raise Http404()

# add notitie
def add_notitie(request, bagregistratie_id):
  title = 'Add Notitie'
  bagregistratie = Bagregistratie.objects.get(id=bagregistratie_id)
  if request.method == "POST":
    form = NotitieForm(request.POST)
    if form.is_valid():
      notitie = form.save(commit=False)
      notitie.author = request.user
      notitie.bagregistratie = bagregistratie
      notitie.save()
      messages.success(request, ("Notitie has been added!"))
      return HttpResponseRedirect('/geoworkflow/bagregistraties/')
  else:
    form = NotitieForm
  context = {
    'title' : title,
    'form'  : form,
  }
  return render(request, 'geoworkflow/add_notitie.html', context)

# add bagregistratie
def add_bagregistratie(request):
  title          = 'add bagregistratie'
  bagobjecttypen = Bagobjecttype.objects.all()
  gemeenten      = Gemeente.objects.all()
  submitted      = False
  if request.method == "POST":
      form = BagregistratieForm(request.POST)
      if form.is_valid():
        bagregistratie = form.save(commit=False)
        bagregistratie.author = request.user
        bagregistratie.save()
        return HttpResponseRedirect('/geoworkflow/bagregistraties/add?submitted=True')
  else:
    # just opening the page; not submitting
      form = BagregistratieForm
  if 'submitted' in request.GET:
    submitted = True
  context = {
    'title'          : title,
    'gemeenten'      : gemeenten,
    'bagobjecttypen' : bagobjecttypen,
    'form'           : form,
    'submitted'      : submitted
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
