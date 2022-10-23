# verwerkingen/views.py

# django
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

# local
from .models import Verwerking

#all verwerkingen classbased
class all_verwerkingenView(ListView):
  model               = Verwerking
  template_name       = 'verwerkingen/all_verwerkingen.html'
  context_object_name = 'verwerkingen_list'
  paginate_by         = 10

  def get_context_data(self, **kwargs):
    context  = super(all_verwerkingenView, self).get_context_data(**kwargs)
    context ['title'] = 'Verwerkingen'
    verwerkingen_list = Verwerking.objects.all()
    context ['aantal']= verwerkingen_list.count()
    paginator         = Paginator(verwerkingen_list, self.paginate_by)
    page_number       = self.request.GET.get('page')
    verwerkingen_page = paginator.get_page(page_number)
    page_count        = "a" * verwerkingen_page.paginator.num_pages
    context ['page_count'] = page_count
    return  context

# show verwerking classbased
class show_verwerkingView(DetailView):
  model               = Verwerking
  template_name       = 'verwerkingen/show_verwerking.html'
  context_object_name = 'verwerking'
  def get_object(self):
    return Verwerking.objects.get(pk=self.kwargs['verwerking_uuid'])
