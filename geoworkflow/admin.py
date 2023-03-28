# geoworkflow/admin.py

# django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# local
from .models import Gemeente

# Register Gemeente
class GemeenteAdmin(ImportExportModelAdmin):
  list_display = ('naam', 'email')
  ordering     = ('naam',)

# overall admin area
admin.site.register(Gemeente, GemeenteAdmin)
