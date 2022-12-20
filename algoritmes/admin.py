# algoritmes/admin.py

# django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# local
from .models import (
  Algoritme
  )

# Register Algoritme
class AlgoritmeAdmin(ImportExportModelAdmin):
  list_display = ('naam',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Algoritme, AlgoritmeAdmin)
