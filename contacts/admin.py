# contacts/admin.py

# django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# local
from .models import Contact

# Register Gemeente
class ContactAdmin(ImportExportModelAdmin):
  list_display = ('name', 'phone')
  ordering     = ('name',)

# overall admin area
admin.site.register(Contact, ContactAdmin)
