# waarmerken/views.py

# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

# local
from .models import Documentwaarmerking

# all Documentwaarmerkingen classbased
class all_documentwaarmerkingenView(ListView):
  model               = Documentwaarmerking
  template_name       = 'waarmerkingen/all_documentwaarmerkingen.html'
  context_object_name = 'documentwaarmerkingen_list'
  paginate_by         = 10

  def get_context_data(self, **kwargs):
    context  = super(all_documentwaarmerkingenView, self).get_context_data(**kwargs)
    context ['title'] = 'Documentwaarmerkingen'
    documentwaarmerkingen_list = Documentwaarmerking.objects.all()
    context ['aantal']= documentwaarmerkingen_list.count()
    paginator         = Paginator(documentwaarmerkingen_list, self.paginate_by)
    page_number       = self.request.GET.get('page')
    documentwaarmerkingen_page = paginator.get_page(page_number)
    page_count        = "a" * documentwaarmerkingen_page.paginator.num_pages
    context ['page_count'] = page_count
    return  context
