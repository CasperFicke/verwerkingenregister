# geoworkflow/urls.py

# django
from django.urls import path

# local
from . import views
#from .views import all_verwerkingenView, show_verwerkingView, edit_verwerkingView

app_name = "geoworkflow"

urlpatterns = [
  # workflow
  path('geoworkflow/'     , views.indexView.as_view(), name='index'),
  ]
