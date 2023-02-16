# reserveren/admin.py

# django
from django.contrib import admin

# local
from .models import Business, Guest, Booking

# Models
admin.site.register(Business)
admin.site.register(Guest)
admin.site.register(Booking)