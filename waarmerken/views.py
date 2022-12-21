# waarmerken/views.py

# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

# local
from .models import Documentwaarmerking, Zaaktype
from .forms import DocumentwaarmerkingForm

# all Documentwaarmerkingen classbased
class all_documentwaarmerkingenView(ListView):
  model               = Documentwaarmerking
  template_name       = 'waarmerken/all_documentwaarmerkingen.html'
  context_object_name = 'documentwaarmerkingen_list'
  paginate_by         = 10

  def get_context_data(self, **kwargs):
    context  = super(all_documentwaarmerkingenView, self).get_context_data(**kwargs)
    context ['title'] = 'Documentwaarmerkingen'
    documentwaarmerkingen_list = Documentwaarmerking.objects.all().order_by('zaaktype')
    context ['aantal']= documentwaarmerkingen_list.count()
    paginator         = Paginator(documentwaarmerkingen_list, self.paginate_by)
    page_number       = self.request.GET.get('page')
    documentwaarmerkingen_page = paginator.get_page(page_number)
    page_count        = "a" * documentwaarmerkingen_page.paginator.num_pages
    context ['page_count'] = page_count
    return  context

# edit documentwaarmerking classbased
class edit_documentwaarmerkingView(UpdateView):
  form_class    = DocumentwaarmerkingForm
  fields        = '__all__'
  template_name = 'waarmerken/edit_documentwaarmerking.html'
  success_url   = 'all-documentwaarmerkingen'

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)

# delete documentwaarmerking functionbased
def delete_documentwaarmerking(request, documentwaarmerking_id):
  documentwaarmerking = Documentwaarmerking.objects.get(id=documentwaarmerking_id)
  if request.user.is_superuser:
    documentwaarmerking.delete()
    messages.success(request, ("Documentwaarmerking " + documentwaarmerking.naam + " has been deleted!"))
    return redirect ('all-documentwaarmerkingen')
  else:
    messages.success(request, ("Documentwaarmerking " + documentwaarmerking.naam + " is not yours to delete!"))
    return redirect ('all-documentwaarmerkingen')

# show zaaktype classbased
class show_zaaktypeView(DetailView):
  model               = Zaaktype
  template_name       = 'waarmerken/show_zaaktype.html'
  context_object_name = 'zaaktype'
  def get_object(self):
    # ophalen van de documentwaarmerkingen van dit zaaktype zodat die ook in de detail-html pagina kunnen worden gepresenteerd
    return Zaaktype.objects.get(pk=self.kwargs['zaaktype_id'])

