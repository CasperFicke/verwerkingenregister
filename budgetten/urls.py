# budgetten/urls.py

# django
from django.urls import path

# local
from . import views

app_name = "budgetten"

urlpatterns = [
  # workflow index
  path('budgetten/'                , views.indexView.as_view(), name='index'),
  path('budgetten/projecten/'      , views.project_list, name='all-projecten'),
  path('budgetten/projecten/add/'  , views.ProjectCreateView.as_view(), name='add-project'),
  path('budgetten/projecten/<slug:project_slug>/'   , views.project_detail, name='show-project')
]