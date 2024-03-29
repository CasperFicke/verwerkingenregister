# bronnen/views.py

# django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

# local
from .models import Bron, Betrokkene, Zaak
#from .forms import BronForm

# index view
# classbased view 
class indexView(TemplateView):
  """
    Bronnen index page.

    **Template:**

    :template:`bronnen/index.html`
  """
  template_name = "bronnen/index.html"

  def get_context_data(self,*args, **kwargs):
    context = super(indexView, self).get_context_data(*args,**kwargs)
    context['title'] = 'Zoeksysteem-Index'
    return context

# all bronnen classbased
class all_bronnenView(ListView):
  model               = Bron
  template_name       = 'bronnen/all_bronnen.html'
  context_object_name = 'bronnen_list'
  paginate_by         = 10

  def get_context_data(self, **kwargs):
    context  = super(all_bronnenView, self).get_context_data(**kwargs)
    context ['title'] = 'Bronnen'
    bronnen_list      = Bron.objects.all().order_by('naam')
    context ['aantal']= bronnen_list.count()
    paginator         = Paginator(bronnen_list, self.paginate_by)
    page_number       = self.request.GET.get('page')
    bronnen_page      = paginator.get_page(page_number)
    page_count        = "a" * bronnen_page.paginator.num_pages
    context ['page_count'] = page_count
    return  context

# delete bron
def delete_bron(request, bron_id):
  item  = Bron.objects.get(id=bron_id)
  item.delete()
  return redirect('bronnen:all-bronnen')

# all zaken classbased
class all_zakenView(ListView):
  model               = Zaak
  template_name       = 'bronnen/all_zaken.html'
  context_object_name = 'zaken_list'
  paginate_by         = 10

  def get_context_data(self, **kwargs):
    context  = super(all_zakenView, self).get_context_data(**kwargs)
    context ['title'] = 'Zaken'
    zaken_list        = Zaak.objects.all()
    context ['aantal']= zaken_list.count()
    paginator         = Paginator(zaken_list, self.paginate_by)
    page_number       = self.request.GET.get('page')
    zaken_page        = paginator.get_page(page_number)
    page_count        = "a" * zaken_page.paginator.num_pages
    context ['page_count'] = page_count
    return  context


# Zoeken view
def zoeken(request):
  context = {}
  if request.method == "POST":
    betrokkene = request.POST['betrokkene']
    if betrokkene is not None:
      try:
        betrokkene_zaak  = Betrokkene.objects.filter(naam__contains = betrokkene).values()[0]
        zaken_betrokkene = Zaak.objects.filter(betrokkene__naam__contains = betrokkene)
        if zaken_betrokkene:
          messages.success(request, ("zoekopdracht uitgevoerd!"))
          context['zaken_betrokkene'] = zaken_betrokkene
          context['betrokkene']       = betrokkene_zaak
          context['aantalzaken']      = zaken_betrokkene.count()
          context['wmozaken']         = zaken_betrokkene.filter(bron__naam__contains = 'WMO').count()
      except:
        messages.success(request, ("geen zaken voor " + betrokkene + " gevonden!"))
      return render(request, 'bronnen/zoeken.html', context)
    else:
      messages.success(request, ("There was an error logging in. Please Try Again..."))
      return redirect('users:login')
  else:
    context ['title'] = 'Zoeken'
    return render(request, 'bronnen/zoeken.html', context)
