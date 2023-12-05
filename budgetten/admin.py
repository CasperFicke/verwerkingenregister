# budgetten/admin.py

# django
from django.contrib import admin

# local
from .models import Project, Expense, Category

admin.site.register(Project)
admin.site.register(Expense)
admin.site.register(Category)