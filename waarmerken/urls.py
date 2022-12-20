# algoritmes/urls.py

# django
from django.urls import path

# local
from . import views
#from .views import all_algoritmesView, show_algoritmeView, edit_algoritmeView

app_name = "waarmerken"

urlpatterns = [
  # Algoritmes
  path('waarmerken/'     , views.all_documentwaarmerkingenView.as_view(), name='all-documentwaarmerkingen'),
  
  ]
