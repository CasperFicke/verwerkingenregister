# verwerkingen/views.py

# django
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.template.response import TemplateResponse
from django.http import HttpResponse, request
from django.core.paginator import Paginator

import json
import csv

# local
from .models import Verwerking, Verwerker, Verwerkersovereenkomst
from .forms import VerwerkingForm, VerwerkersovereenkomstForm
from datetime import datetime, timedelta, date

# index view classbased
class indexView(TemplateView):
  template_name = "verwerkingen/index.html"

  def get_context_data(self, **kwargs):
    context = super(indexView, self).get_context_data(**kwargs)
    context['title'] = 'Beheer Verwerkingen'
    return context

# all verwerkingen classbased
class all_verwerkingenView(ListView):
  model               = Verwerking
  template_name       = 'verwerkingen/all_verwerkingen.html'
  context_object_name = 'verwerkingen_list'
  paginate_by         = 10

  def get_context_data(self, **kwargs):
    context           = super(all_verwerkingenView, self).get_context_data(**kwargs)
    context ['title'] = 'Verwerkingen'
    verwerkingen_list = Verwerking.objects.all()
    context ['aantal']= verwerkingen_list.count()
    paginator         = Paginator(verwerkingen_list, self.paginate_by)
    page_number       = self.request.GET.get('page')
    verwerkingen_page = paginator.get_page(page_number)
    page_count        = "a" * verwerkingen_page.paginator.num_pages
    context ['page_count'] = page_count
    return  context

# all verwerkingen mavim functionbased
def all_verwerkingen_mavimView(request):
  title = 'mavim verwerkingen'
  # mavimverwerkingen
  #verwerkingen = os.path.join('data', '20230606_Verwerwerkingsaktiviteiten.json')
  # Opening JSON file
  with open('data/20230606_Verwerwerkingsaktiviteiten.json') as json_file:
    data = json.load(json_file)
    # print(data[:2])
    # Print the type of data variable
    # print("Type:", type(data))
  context = {
    'title'       : title,
    'verwerkingen': data
  }
  return TemplateResponse(request, 'verwerkingen/all_verwerkingen_mavim.html', context)
  
# show verwerking classbased
class show_verwerkingView(DetailView):
  model               = Verwerking
  template_name       = 'verwerkingen/show_verwerking.html'
  context_object_name = 'verwerking'
  def get_object(self):
    return Verwerking.objects.get(pk=self.kwargs['verwerking_uuid'])

# add verwerking classbased
class add_verwerkingView(LoginRequiredMixin, CreateView):
  model         = Verwerking
  fields        = '__all__'
  template_name = 'verwerkingen/add_verwerking.html'
  success_url   = '/verwerkingen/'

# edit verwerking classbased
class edit_verwerkingView(UpdateView):
  form_class    = VerwerkingForm
  fields        = '__all__'
  template_name = 'verwerkingen/edit_verwerking.html'
  success_url   = 'all-verwerkingen'

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)

# delete verwerking classbased
# class delete_verwerkingView(DeleteView):
#   model         = Verwerking
#   success_url = reverse_lazy('all-verwerkingen')
 
# delete verwerking functionbased
def delete_verwerking(request, verwerking_uuid):
  verwerking = Verwerking.objects.get(uuid=verwerking_uuid)
  if request.user.is_superuser:
    verwerking.delete()
    messages.success(request, ("Verwerking " + verwerking.naam + " has been deleted!"))
    return redirect ('verwerkingen:all-verwerkingen')
  else:
    messages.success(request, ("Verwerking " + verwerking.naam + " is not yours to delete!"))
    return redirect ('verwerkingen:all-verwerkingen')


# all verwerkers classbased
class all_verwerkersView(ListView):
  model               = Verwerker
  template_name       = 'verwerkingen/all_verwerkers.html'
  context_object_name = 'verwerkers_list'
  paginate_by         = 10

  def get_context_data(self, **kwargs):
    context           = super(all_verwerkersView, self).get_context_data(**kwargs)
    context ['title'] = 'Verwerkers'
    verwerkers_list   = Verwerker.objects.all()
    context ['aantal']= verwerkers_list.count()
    paginator         = Paginator(verwerkers_list, self.paginate_by)
    page_number       = self.request.GET.get('page')
    verwerkers_page   = paginator.get_page(page_number)
    page_count        = "a" * verwerkers_page.paginator.num_pages
    context ['page_count'] = page_count
    return  context

# export verwerkers to CSV
def csv_verwerkers(request):
  response= HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename=VerwerkersList_' + str(date.today()) + '.csv'
  # create CSV writer
  writer=csv.writer(response)
  # Select all verwerkers to export
  verwerkers_list = Verwerker.objects.all()
  # create first row with column headings
  writer.writerow(['Naam', 'Beschrijving'])
  # loop thru and output
  for verwerker in verwerkers_list:
    writer.writerow([verwerker.naam, verwerker.beschrijving])
  return response

# show verwerker classbased
class show_verwerkerView(DetailView):
  model               = Verwerker
  template_name       = 'verwerkingen/show_verwerker.html'
  context_object_name = 'verwerker'
  def get_object(self):
    return Verwerker.objects.get(pk=self.kwargs['verwerker_id'])
  
# Add verwerker
class VerwerkerCreateView(CreateView):
  model         = Verwerker
  template_name = 'verwerkingen/verwerkerform.html'
  fields        = ['naam', 'beschrijving']
  success_url   = reverse_lazy('verwerkingen:all-verwerkers')

# Update verwerker
class VerwerkerUpdateView(UpdateView):
  model         = Verwerker
  template_name = 'verwerkingen/verwerkerform.html'
  fields        = ['naam', 'beschrijving']

# Delete verwerker
class VerwerkerDeleteView(DeleteView):
  model         = Verwerker
  template_name = 'verwerkingen/verwerker_confirm_delete.html'
  success_url   = reverse_lazy('verwerkingen:all-verwerkers')

# all verwerkersovereenkomsten
def all_verwerkersovereenkomsten(request):
  title       = 'verwerkersovereenkomsten'
  verwerkersovereenkomsten_list  = Verwerkersovereenkomst.objects.all().order_by('naam')
  verwerkersovereenkomsten_count = verwerkersovereenkomsten_list.count()
  submitted = False
  if request.method == "POST":
    form = VerwerkersovereenkomstForm(request.POST, request.FILES)
    if form.is_valid():
      verwerkersovereenkomst = form.save()
  else:
    form = VerwerkersovereenkomstForm
    if 'submitted' in request.GET:
      submitted = True
 
  # Set up pagination
  paginator    = Paginator(verwerkersovereenkomsten_list, 5) # Show 5 verwerkersovereenkomsten per page.
  page_number  = request.GET.get('page')
  verwerkersovereenkomsten_page  = paginator.get_page(page_number)
  page_count   = "a" * verwerkersovereenkomsten_page.paginator.num_pages
  is_paginated = verwerkersovereenkomsten_page.has_other_pages

  context  = {
    'title'        : title,
    'form'         : form,
    'submitted'    : submitted,
    'verwerkersovereenkomsten_list': verwerkersovereenkomsten_list,
    'aantal'       : verwerkersovereenkomsten_count,
    'page_obj'     : verwerkersovereenkomsten_page,
    'is_paginated' : is_paginated,
    'page_count'   : page_count
  }
  return TemplateResponse(request, 'verwerkingen/all_verwerkersovereenkomsten.html', context)
  
# show verwerkersovereenkomst classbased
class show_verwerkersovereenkomstView(DetailView):
  model               = Verwerkersovereenkomst
  template_name       = 'verwerkingen/show_verwerkersovereenkomst.html'
  context_object_name = 'verwerkersovereenkomst'
  def get_object(self):
    return Verwerkersovereenkomst.objects.get(pk=self.kwargs['verwerkersovereenkomst_id'])

# Delete verwerkersovereenkomst
class VerwerkersovereenkomstDeleteView(DeleteView):
  model         = Verwerkersovereenkomst
  template_name = 'verwerkingen/verwerkersovereenkomst_confirm_delete.html'
  success_url   = reverse_lazy('verwerkingen:all-verwerkersovereenkomsten')
