# budgetten/urls.py

# django
from django.urls import path

# local
from . import views

app_name = "budgetten"

urlpatterns = [
  # workflow index
  path('budgetten/'          , views.indexView.as_view(), name='index'),
]