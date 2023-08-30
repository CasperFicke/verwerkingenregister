# site_basis/views.py

from django.views import generic

# home view classbased
class HomeView(generic.TemplateView):
  """
    Website home page.

    **Template:**

    :template:`site_basis/index.html`
    """
  template_name = "site_basis/index.html"
	
  def get_context_data(self, **kwargs):
    context = super(HomeView, self).get_context_data(**kwargs)
    context['title'] = 'Registers beheer'
    return context



