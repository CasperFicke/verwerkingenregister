# budgetten/views.py

# django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from django.utils.text import slugify

import json

# local
from .models import Project, Category, Expense
from .forms import ExpenseForm

# index view
class indexView(TemplateView):
	"""
    Budgetten index page.

    **Template:**

    :template:`budgetten/index.html`
    """
	template_name = "budgetten/index.html"

# All projects
def project_list(request):
  project_list = Project.objects.all()
  return render(request, 'budgetten/project-list.html', {'project_list': project_list})

# Show project
def project_detail(request, project_slug):
  project = get_object_or_404(Project, slug=project_slug)

  if request.method == 'GET':
    category_list = Category.objects.filter(project=project)
    return render(request, 'budgetten/project-detail.html', {'project': project, 'expense_list': project.expenses.all(), 'category_list': category_list})

  elif request.method == 'POST':
    form = ExpenseForm(request.POST)

    if form.is_valid():
      title         = form.cleaned_data['title']
      amount        = form.cleaned_data['amount']
      category_name = form.cleaned_data['category']
      category      = get_object_or_404(Category, project=project, name=category_name)

      Expense.objects.create(
        project  = project,
        title    = title,
        amount   = amount,
        category = category
      )

  elif request.method == 'DELETE':
    id      = json.loads(request.body)['id']
    expense = Expense.objects.get(id=id)
    expense.delete()
    return HttpResponse(status=204)

  return redirect(project)

# Add project
class ProjectCreateView(CreateView):
  model         = Project
  template_name = 'budgetten/add-project.html'
  fields        = ('name', 'budget')

  def form_valid(self, form):
    self.object = form.save()
    categories  = self.request.POST.get('categoriesString').split(',')
    for category in categories:
      Category.objects.create(
        project = Project.objects.get(id=self.object.id),
        name    = category
      )
    return redirect(self.object)