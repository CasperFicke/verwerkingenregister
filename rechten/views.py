# rechten/views.py

# django
from django.views import generic
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

# local
from .models import Rol

# rechten-index view classbased
class all_rechtenView(generic.TemplateView):
	"""
    Datasaets index page.

    **Template:**

    :template:`rechten/rechten_index.html`
    """
	template_name = "rechten/rechten_index.html"
  
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"]    = 'rechten-index'
		return context

# all rollen classbased
class all_rollenView(ListView):
  model               = Rol
  template_name       = 'rechten/all_rollen.html'
  context_object_name = 'rollen_list'
  paginate_by         = 10

  def get_context_data(self, **kwargs):
    context  = super(all_rollenView, self).get_context_data(**kwargs)
    context ['title'] = 'Rollen'
    rollen_list = Rol.objects.all()
    context ['aantal']= rollen_list.count()
    paginator         = Paginator(rollen_list, self.paginate_by)
    page_number       = self.request.GET.get('page')
    rollen_page       = paginator.get_page(page_number)
    page_count        = "a" * rollen_page.paginator.num_pages
    context ['page_count'] = page_count
    return  context

# show rol classbased
class show_rolView(DetailView):
  model               = Rol
  template_name       = 'rechten/show_rol.html'
  context_object_name = 'rol'
  def get_object(self):
    return Rol.objects.get(pk=self.kwargs['rol_uuid'])
