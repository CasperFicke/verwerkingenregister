# geoworkflow/admin.py

# django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# local
from .models import (
  Gemeente,
  Straat,
  Bagobjecttype,
  Baggebeurtenis,
  Bagregistratie,
  Notitie,
  Status
  )

# GEO workflow admin area
class GEOworkflowAdminArea(admin.AdminSite):
  site_header = 'GEO-workflow Admin Area'
  index_title = "GEO-workflow Admin"
  site_title  = "GEOworkflow"

GEOworkflow_adminsite = GEOworkflowAdminArea(name = 'GEOworkflowAdmin')

# Models

# Register Gemeente
class GemeenteAdmin(ImportExportModelAdmin):
  list_display = ('naam', 'email')
  ordering     = ('naam',)
# overall admin area
admin.site.register(Gemeente, GemeenteAdmin)

# Register Straat
class StraatAdmin(ImportExportModelAdmin):
  list_display = ('gemeente', 'naam')
  ordering     = ('gemeente', 'naam',)
# overall admin area
admin.site.register(Straat, StraatAdmin)

# Register BAGobjecttype
class BAGobjecttypeAdmin(ImportExportModelAdmin):
  ordering     = ('naam',)
# overall admin area
admin.site.register(Bagobjecttype, BAGobjecttypeAdmin)

# Register BAGgebeurtenis
class BAGgebeurtenisAdmin(ImportExportModelAdmin):
  list_display = ('naam', 'bagobjecttype')
  ordering     = ('bagobjecttype', 'naam',)
# overall admin area
admin.site.register(Baggebeurtenis, BAGgebeurtenisAdmin)

# Register BAGregistratie
class BAGregistratieAdmin(ImportExportModelAdmin):
  list_display = ('gemeente', 'straat', 'volledig_ontvangen')
  ordering     = ('gemeente',)
# overall admin area
admin.site.register(Bagregistratie, BAGregistratieAdmin)

class NotitieAdmin(admin.ModelAdmin):
  list_display = ('title', 'author')
  ordering     = ('date_added',)
# overall admin area
admin.site.register(Notitie, NotitieAdmin)

# Register Status
class StatusAdmin(ImportExportModelAdmin):
  list_display = ('registratie', 'naam' )
  ordering     = ('registratie', 'naam',)
# overall admin area
admin.site.register(Status, StatusAdmin)