# budgetten/views.py

# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator


# local
#from .models import 
#from .forms import 

# index view
class indexView(TemplateView):
	"""
    Budgetten index page.

    **Template:**

    :template:`budgetten/index.html`
    """
	template_name = "budgetten/index.html"