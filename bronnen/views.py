# bronnen/views.py

# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

# local
from .models import Bron
#from .forms import BronForm

# all bronnen classbased
class all_bronnenView(ListView):
  model               = Bron
  template_name       = 'bronnen/all_bronnen.html'
  context_object_name = 'bronnen_list'
  paginate_by         = 10

  def get_context_data(self, **kwargs):
    context  = super(all_bronnenView, self).get_context_data(**kwargs)
    context ['title'] = 'Bronnen'
    bronnen_list      = Bron.objects.all()
    context ['aantal']= bronnen_list.count()
    paginator         = Paginator(bronnen_list, self.paginate_by)
    page_number       = self.request.GET.get('page')
    bronnen_page      = paginator.get_page(page_number)
    page_count        = "a" * bronnen_page.paginator.num_pages
    context ['page_count'] = page_count
    return  context
