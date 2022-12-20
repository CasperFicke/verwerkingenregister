# waarmerken/admin.py

# Django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Local
from .models import (
  Zaaktype,
  Documenttype,
  Waarmerkniveau,
  Documentwaarmerking
  )

# Register Zaaktype
class ZaaktypeAdmin(admin.ModelAdmin):
  list_display = ('naam',)
 
# overall admin area
admin.site.register(Zaaktype, ZaaktypeAdmin)

# Register Documenttype
class DocumenttypeAdmin(admin.ModelAdmin):
  list_display = ('naam',)
# overall admin area
admin.site.register(Documenttype, DocumenttypeAdmin)

# Register Waarmerkniveau
class WaarmerkniveauAdmin(admin.ModelAdmin):
  list_display = ('naam',)
# overall admin area
admin.site.register(Waarmerkniveau, WaarmerkniveauAdmin)


# Register Documentwaarmerking
class DocumentwaarmerkingAdmin(admin.ModelAdmin):
  list_display = ('naam',)
# overall admin area
admin.site.register(Documentwaarmerking, DocumentwaarmerkingAdmin)