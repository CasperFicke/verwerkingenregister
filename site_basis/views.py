# site_basis/views.py

from django.shortcuts import render, redirect, get_object_or_404
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


# about
def aboutView(request):
  title = 'about'
  context = {
    'title' : title,
  }
  return render(request, 'site_basis/about.html', context)

# contact
def contactView(request):
  title = 'contact'
  context = {
    'title' : title,
  }
  return render(request, 'site_basis/contact.html', context)

# privacy
def privacyView(request):
  title = 'privacy'
  context = {
    'title' : title,
  }
  return render(request, 'site_basis/privacy.html', context)