# contacts/urls.py

# django
from django.urls import path

# local
from . import views

app_name = "contacts"

urlpatterns = [
  # contacten
  path('contacts/'            , views.indexView, name='index'),
  path('contacts/create-form' , views.create_contact, name='create-contact'),
  ]
