# rechten/urls.py

# django
from django.urls import path

# local
from . import views
from .views import all_rollenView, show_rolView


app_name = "rechten"

urlpatterns = [
  # Verwerkingen
  path('rechten/'           , views.all_rechtenView.as_view(), name='all-rechten'),
  path('rollen/'            , all_rollenView.as_view(), name='all-rollen'),
  path('rollen/<rol_uuid>/' , show_rolView.as_view(), name='show-rol'),
  ]
