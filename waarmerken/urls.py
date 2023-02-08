# algoritmes/urls.py

# django
from django.urls import path

# local
from . import views
from .views import indexView, edit_documentwaarmerkingView, show_zaaktypeView

app_name = "waarmerken"

urlpatterns = [
  # documentwaarmerkingen
  path('waarmerken/'                                , views.indexView.as_view(), name='index'),
  path('waarmerken/zaaktypen/'                      , views.all_zaaktypenView.as_view(), name='all-zaaktypen'),
  #path('waarmerken/documenttypen/'                  , views.all_documenttypenView.as_view(), name='all-documenttypen'),
  path('waarmerken/documentwaarmerkingen/'          , views.all_documentwaarmerkingenView.as_view(), name='all-documentwaarmerkingen'),
  path('waarmerken/<documentwaarmerking_id>/edit/'  , edit_documentwaarmerkingView.as_view(), name='edit-documentwaarmerking'),
  path('waarmerken/<documentwaarmerking_id>/delete/', views.delete_documentwaarmerking, name="delete-documentwaarmerking"),
  path('waarmerken/<zaaktype_id>'                   , show_zaaktypeView.as_view(), name="show-zaaktype"),
  ]
