# bronnen/admin.py

# django
from django.contrib import admin

# local
from .models import (
  Bron,
  Betrokkene,
  Zaak
  )

# Register Bron
class BronAdmin(admin.ModelAdmin):
  list_display = ('naam', 'beschrijving',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Bron, BronAdmin)

# Register Models without layout:
myModels = [Betrokkene, Zaak]
# overall adminarea
admin.site.register(myModels)