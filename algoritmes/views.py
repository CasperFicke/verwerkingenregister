# algoritmes/views.py

# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

# local
from .models import Algoritme
from .forms import AlgoritmeForm

# all verwerkingen classbased
class all_algoritmesView(ListView):
  model               = Algoritme
  template_name       = 'algoritmes/all_algoritmes.html'
  context_object_name = 'algoritmes_list'
  paginate_by         = 10

  def get_context_data(self, **kwargs):
    context  = super(all_algoritmesView, self).get_context_data(**kwargs)
    context ['title'] = 'Algoritmes'
    algoritmes_list = Algoritme.objects.all()
    context ['aantal']= algoritmes_list.count()
    paginator         = Paginator(algoritmes_list, self.paginate_by)
    page_number       = self.request.GET.get('page')
    algoritmes_page = paginator.get_page(page_number)
    page_count        = "a" * algoritmes_page.paginator.num_pages
    context ['page_count'] = page_count
    return  context

# show algoritme classbased
class show_algoritmeView(DetailView):
  model               = Algoritme
  template_name       = 'algoritmes/show_algoritme.html'
  context_object_name = 'algoritme'
  def get_object(self):
    return Algoritme.objects.get(pk=self.kwargs['algoritme_id'])

# add algoritme classbased
class add_algoritmeView(LoginRequiredMixin, CreateView):
  model         = Algoritme
  fields        = '__all__'
  template_name = 'algoritmes/add_algoritme.html'
  success_url   = '/algoritmes/'

# edit algoritme classbased
class edit_algoritmeView(UpdateView):
  form_class    = AlgoritmeForm
  fields        = '__all__'
  template_name = 'algoritmes/edit_algoritme.html'
  success_url   = 'all-algoritmes'

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)

# delete algoritme classbased
# class delete_algoritmeView(DeleteView):
#   model         = Algoritme
#   success_url = reverse_lazy('all-algoritmes')
 
# delete algoritme functionbased
def delete_algoritme(request, algoritme_id):
  algoritme = Algoritme.objects.get(id=algoritme_id)
  if request.user.is_superuser:
    algoritme.delete()
    messages.success(request, ("Algoritme " + algoritme.naam + " has been deleted!"))
    return redirect ('algoritmes:all-algoritmes')
  else:
    messages.success(request, ("Algoritme " + algoritme.naam + " is not yours to delete!"))
    return redirect ('all-algoritmes')
