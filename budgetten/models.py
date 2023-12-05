# budgetten/models.py

# django
from django.db import models
from django.utils.text import slugify

# Project model
class Project(models.Model):
  class Meta:
    ordering            = ['name']
    verbose_name        = 'project'
    verbose_name_plural = 'projects'
  # attributes
  name   = models.CharField(max_length=100)
  slug   = models.SlugField(max_length=100, unique=True, blank=True)
  budget = models.IntegerField()

  # 
  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Project, self).save(*args, **kwargs)

  # nog te besteden budget
  @property
  def budget_left(self):
    expense_list = Expense.objects.filter(project=self)
    total_expense_amount = 0
    for expense in expense_list:
      total_expense_amount += expense.amount

    # temporary solution, because the form currently only allows integer amounts
    total_expense_amount = int(total_expense_amount)

    return self.budget - total_expense_amount

  # totaal aantal transacties 
  @property
  def total_transactions(self):
    expense_list = Expense.objects.filter(project=self)
    return len(expense_list)

  def get_absolute_url(self):
    return '/budgetten/projecten/' + self.slug
  # functie om object in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.name}'

# Category model
class Category(models.Model):
  class Meta:
    ordering            = ['name']
    verbose_name        = 'category'
    verbose_name_plural = 'categories'
  # attributes
  name    = models.CharField(max_length=50)
  # relaties
  project = models.ForeignKey(Project, on_delete=models.CASCADE)

  # functie om object in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.name}'

# Expense model
class Expense(models.Model):
  class Meta:
    ordering            = ('-amount',)
    verbose_name        = 'expense'
    verbose_name_plural = 'expenses'
  # attributes
  title    = models.CharField(max_length=100)
  amount   = models.DecimalField(max_digits=8, decimal_places=2)
  # relaties
  project  = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
  # functie om object in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.title}'