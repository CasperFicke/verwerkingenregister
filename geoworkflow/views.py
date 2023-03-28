# geoworkflow/views.py

# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

# local
#from .models import Verwerking
#from .forms import VerwerkingForm

# index view
# classbased view 
class indexView(TemplateView):
	"""
    Geoworkflow index page.

    **Template:**

    :template:`geoworkflow/index.html`
    """
	template_name = "geoworkflow/index.html"
