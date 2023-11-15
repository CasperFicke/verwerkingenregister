# site_basis/urls.py

# django
from django.urls import path

# local
from . import views

app_name = "site_basis"

urlpatterns = [
	path(''         , views.HomeView.as_view() , name="home"),
  path('about/'   , views.aboutView          , name="about"),
  path('contact/' , views.contactView        , name="contact"),
  path('privacy/' , views.privacyView        , name="privacy"),
]