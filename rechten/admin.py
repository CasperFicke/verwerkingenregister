
# django
from django.contrib import admin

# local
from .models import (
  Rol,
  Verwerkingattribuut
  )

# Register Verordening Rol
class RolAdmin(admin.ModelAdmin):
  list_display = ('naam', 'beschrijving',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Rol, RolAdmin)

# Register Verordening attribuut
class VerwerkingattribuutAdmin(admin.ModelAdmin):
  list_display = ('naam', 'beschrijving',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Verwerkingattribuut, VerwerkingattribuutAdmin)
