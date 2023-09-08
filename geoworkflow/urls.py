# geoworkflow/urls.py

# django
from django.urls import path

# local
from . import views
#from .views import all_verwerkingenView, show_verwerkingView, edit_verwerkingView

app_name = "geoworkflow"

urlpatterns = [
  # workflow index
  path('geoworkflow/'                    , views.indexView.as_view(), name='index'),

  path('geoworkflow/bagregistraties/'    , views.bagregistraties, name='all-bagregistraties'),
  
  # CRUD single bagregistratie
  path('geoworkflow/bagregistraties/add'                 , views.add_bagregistratie, name='add-bagregistratie'),
  path('geoworkflow/bagregistraties/<bagregistratie_id>' , views.show_bagregistratie, name="show-bagregistratie"),
  
  # notities bij bagregistratie
  path('geoworkflow/bagregistraties/<bagregistratie_id>/notities/add/' , views.add_notitie, name='add-notitie'),

  # gemeente / straat
  #path('geoworkflow/gemeenten/'         , views.gemeenten, name='gemeenten'),
  path('geoworkflow/straten/'            , views.straten, name='straten'),
  
  # bagobject / baggebeurtenis
  #path('geoworkflow/bagobjecttypen/'     , views.bagobjecttypen, name='bagobjecttypen'),
  path('geoworkflow/baggebeurtenissen/'  , views.baggebeurtenissen, name='baggebeurtenissen'),
  ]
