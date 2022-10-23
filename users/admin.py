# users/admin.py

# django
from django.contrib import admin

# local
from .models import UserProfile

# Register UserProfile
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('bio', 'country',)

# overall admin area
admin.site.register(UserProfile, UserProfileAdmin)
