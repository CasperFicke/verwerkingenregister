# rechten/urls.py

# django
from django.urls import path

# local
from . import views


app_name = "rechten"

urlpatterns = [
  # Verwerkingen
  path('rechten/'  , views.AllRechtenView.as_view(), name='all-rechten'),
 
  ]
