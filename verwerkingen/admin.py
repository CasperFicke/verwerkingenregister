# verwerkingen/admin.py

# django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# local
from .models import (
  Gemeente,
  Verordening,
  Ontvanger,
  Verantwoordelijke,
  Team,
  Grondslag,
  Persoonsgegeven,
  Verwerker,
  Verwerkersovereenkomst,
  Betrokkene,
  Ontvanger,
  Hoofdproces,
  Verwerking
  )

# Register Verordening
class VerordeningAdmin(ImportExportModelAdmin):
  list_display = ('naam', 'beschrijving',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Verordening, VerordeningAdmin)

# Register Verantwoordelijke
class VerantwoordelijkeAdmin(ImportExportModelAdmin):
  list_display = ('naam',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Verantwoordelijke, VerantwoordelijkeAdmin)

# Register Grondslag
class GrondslagAdmin(ImportExportModelAdmin):
  list_display = ('naam',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Grondslag, GrondslagAdmin)

# Register Persoonsgegeven
class PersoonsgegevenAdmin(ImportExportModelAdmin):
  list_display = ('type', 'beschrijving',)
  ordering     = ('type',)
# overall admin area
admin.site.register(Persoonsgegeven, PersoonsgegevenAdmin)

# Register Verwerkersovereenkomst
class VerwerkersovereenkomstAdmin(admin.ModelAdmin):
  list_display = ('naam', 'verwerker', 'pdf', 'extern',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Verwerkersovereenkomst, VerwerkersovereenkomstAdmin)

# Register Verwerking
class VerwerkingAdmin(ImportExportModelAdmin):
  list_display = ('naam', 'doel', 'hoofdproces', 'buitenEUgedeeld', 'dpia_uitgevoerd',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Verwerking, VerwerkingAdmin)

# inline
class InLineVerwerking(admin.StackedInline):
  model = Verwerking
  extra = 0

# Register Betrokkene
class BetrokkeneAdmin(ImportExportModelAdmin):
  list_display = ('naam', 'beschrijving',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Betrokkene, BetrokkeneAdmin)

# Register Hoofdproces
class HoofdprocesAdmin(ImportExportModelAdmin):
  list_display = ('naam',)
  ordering     = ('naam',)
  inlines      = [InLineVerwerking]
# overall admin area
admin.site.register(Hoofdproces, HoofdprocesAdmin)

# Register Models without layout:
myModels = [Gemeente, Team, Verwerker, Ontvanger]
# overall adminarea
admin.site.register(myModels)