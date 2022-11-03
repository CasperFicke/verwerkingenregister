# rechten/views.py

from django.shortcuts import render
from django.views import generic
  
# datasets-index view
# classbased view 
class AllRechtenView(generic.TemplateView):
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

