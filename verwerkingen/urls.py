# verwerkingen/urls.py

# django
from django.urls import path

# local
from . import views
from .views import all_verwerkingenView, show_verwerkingView

app_name = "verwerkingen"

urlpatterns = [
  # Verwerkingen
  path('verwerkingen/'                   , views.all_verwerkingenView.as_view(), name='all-verwerkingen'),
  path('verwerkingen/<verwerking_uuid>/' , show_verwerkingView.as_view(), name='show-verwerking'),
  ]

  