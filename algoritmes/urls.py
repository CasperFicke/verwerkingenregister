# algoritmes/urls.py

# django
from django.urls import path

# local
from . import views
from .views import all_algoritmesView, show_algoritmeView, edit_algoritmeView

app_name = "algoritmes"

urlpatterns = [
  # Algoritmes
  path('algoritmes/'                        , views.all_algoritmesView.as_view(), name='all-algoritmes'),
  path('algoritmes/add/'                    , views.add_algoritmeView.as_view(), name="add-algoritme"),
  path('algoritmes/<algoritme_id>/'       , show_algoritmeView.as_view(), name='show-algoritme'),
  path('algoritmes/<algoritme_id>/edit/'  , edit_algoritmeView.as_view(), name='edit-algoritme'),
  #path('algoritmes/<algoritme_id>/delete/', views.delete_algoritmeView.as_view(), name="delete-algoritme"), classbased
  path('algoritmes/<algoritme_id>/delete/', views.delete_algoritme, name="delete-algoritme"),
  ]
