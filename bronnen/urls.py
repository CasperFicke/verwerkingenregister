# bronnen/urls.py

# django
from django.urls import path

# local
from . import views
from .views import all_bronnenView

app_name = "bronnen"

urlpatterns = [
  # Bronnen
  path('bronnen/'                     , views.indexView.as_view(), name='index'),
  path('bronnen/bronnen/'             , views.all_bronnenView.as_view(), name='all-bronnen'),
  path('bronnen/zaken/'               , views.all_zakenView.as_view(), name='all-zaken'),
  path('bronnen/zoeken/'              , views.zoeken, name='zoeken'),
  
  # CRUD bron
  #path('bronnen/add/'                , views.add_bronView.as_view(), name="add-bron"),
  #path('bronnen/<bron_id>/'          , views.show_bron, name='show-bron'),
  #path('bronnen/<bron_id>/edit/'     , views.edit_bron, name='edit-bron'),
  path('bronnen/<bron_id>/delete/'    , views.delete_bron, name="delete-bron"),
  ]
