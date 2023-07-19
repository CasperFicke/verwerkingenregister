# verwerkingen/urls.py

# django
from django.urls import path

# local
from . import views
from .views import (
  show_verwerkingView,
  edit_verwerkingView,
  all_verwerkersView,
  show_verwerkerView,
  VerwerkerCreateView,
  VerwerkerUpdateView,
  VerwerkerDeleteView,
  all_verwerkersovereenkomsten,
  show_verwerkersovereenkomstView,
  VerwerkersovereenkomstDeleteView)

app_name = "verwerkingen"

urlpatterns = [
  # Verwerkingen
  path('verwerkingen/'                                      , views.indexView.as_view(), name='index'),
  path('verwerkingen/verwerkingen/'                         , views.all_verwerkingenView.as_view(), name='all-verwerkingen'),
  path('verwerkingen/verwerkingen/add/'                     , views.add_verwerkingView.as_view(), name="add-verwerking"),
  path('verwerkingen/verwerkingen/<verwerking_uuid>/'       , show_verwerkingView.as_view(), name='show-verwerking'),
  path('verwerkingen/verwerkingen/<verwerking_uuid>/edit/'  , edit_verwerkingView.as_view(), name='edit-verwerking'),
  #path('verwerkingen/<verwerking_uuid>/delete/'            , views.delete_verwerkingView.as_view(), name="delete-verwerking"), classbased
  path('verwerkingen/verwerkingen/<verwerking_uuid>/delete/', views.delete_verwerking, name="delete-verwerking"),
  # mavim verwerkingen
  path('verwerkingen/mavimverwerkingen/'                    , views.all_verwerkingen_mavimView, name='all-verwerkingen-mavim'),
  # verwerkers
  path('verwerkingen/verwerkers/'                           , all_verwerkersView.as_view(), name='all-verwerkers'),
  path('verwerkingen/verwerkers/csv/'                       , views.csv_verwerkers, name="csv-verwerkers"),
  path('verwerkingen/verwerkers/<verwerker_id>/'            , show_verwerkerView.as_view(), name='show-verwerker'),
  path('verwerkingen/verwerkers/add'                        , VerwerkerCreateView.as_view(), name="add-verwerker"),
  path('verwerkingen/verwerkers/<int:pk>/update'            , VerwerkerUpdateView.as_view(), name="update-verwerker"),
  path('verwerkingen/verwerkers/<int:pk>/delete'            , VerwerkerDeleteView.as_view(), name="delete-verwerker"),
  # verwerkersovereenkomsten
  #path('verwerkingen/verwerkersovereenkomsten/'             , views.all_verwerkersovereenkomstenView.as_view(), name='all-verwerkersovereenkomsten'),
  path('verwerkingen/verwerkersovereenkomsten/'             , views.all_verwerkersovereenkomsten, name='all-verwerkersovereenkomsten'),
  path('verwerkingen/verwerkersovereenkomsten/<verwerkersovereenkomst_id>/' , show_verwerkersovereenkomstView.as_view(), name='show-verwerkersovereenkomst'),
  path('verwerkingen/verwerkersovereenkomsten/<int:pk>/delete' , VerwerkersovereenkomstDeleteView.as_view(), name="delete-verwerkersovereenkomst"),
  ]
