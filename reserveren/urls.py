# reserveren/urls.py

# django
from django.urls import path

# local
from . import views
from .views import BookingWizardView

app_name = "reserveren"

urlpatterns = [
  path('reserveren/'    , views.BookingWizardView.as_view(), name='maak_reservering'),
]