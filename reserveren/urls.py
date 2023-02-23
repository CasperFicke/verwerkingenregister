# reserveren/urls.py

# django
from django.urls import path

# local
from . import views
from .views import BookingWizardView
from .forms import GuestForm

app_name = "reserveren"

urlpatterns = [
  path('reserveren/'          , views.BookingWizardView.as_view(), name='maak-reservering'),
  path('reserveren/preview/'  , views.GuestFormPreview(GuestForm), name='preview'),
]