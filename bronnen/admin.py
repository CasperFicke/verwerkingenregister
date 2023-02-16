# bronnen/admin.py

# django
from django.contrib import admin

# local
from .models import (
  Bron,
  Betrokkene,
  Zaak,
  Zoekvraag,
  )

# Register Bron
class BronAdmin(admin.ModelAdmin):
  list_display = ('naam', 'beschrijving',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Bron, BronAdmin)

# Register Betrokkene
class BetrokkeneAdmin(admin.ModelAdmin):
  list_display = ('naam', 'postcode', 'huisnummer',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Betrokkene, BetrokkeneAdmin)

# Register Zaak
class ZaakAdmin(admin.ModelAdmin):
  list_display = ('zaakonderwerp', 'bron', 'zaaktype', 'betrokkene', 'casemanager',)
  ordering     = ('zaakonderwerp',)
# overall admin area
admin.site.register(Zaak, ZaakAdmin)

# Register Zoekvraag
class ZoekvraagAdmin(admin.ModelAdmin):
  list_display = ('naam', 'betrokkene',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Zoekvraag, ZoekvraagAdmin)


# Register Models without layout:
#myModels = []
# overall admin area
#admin.site.register(myModels)