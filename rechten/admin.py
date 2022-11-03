
# django
from django.contrib import admin

# local
from .models import (
  Rol
  )

# Register Verordening
class RolAdmin(admin.ModelAdmin):
  list_display = ('naam', 'beschrijving',)
  ordering     = ('naam',)
# overall admin area
admin.site.register(Rol, RolAdmin)
