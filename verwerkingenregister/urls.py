# verwerkigenregister/urls.py

# django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  # App urls
  path('', include('site_basis.urls'  , namespace="site-basis")),
  path('', include('users.urls'       , namespace="users")),
  path('', include('rechten.urls'     , namespace="rechten")),
  path('', include('verwerkingen.urls', namespace="verwerkingen")),
  path('', include('algoritmes.urls'  , namespace="algoritmes")),
  path('', include('waarmerken.urls'  , namespace="waarmerken")),
  path('', include('bronnen.urls'     , namespace="bronnen")),
  path('', include('geoworkflow.urls' , namespace="geoworkflow")),
  path('', include('reserveren.urls'  , namespace="reserveren")),
  # debug urls
  #path("__debug__", include('debug_toolbar.urls')),
]

# Configure Admin area Titles
admin.site.site_header = "Registers Administration"      # header op admin pagina (blauwe balk)
admin.site.index_title = "Site Admin" # koptekst op admin pagina en 1e deel in browsertab title
admin.site.site_title  = "Registers" # toevoeging (2e deel) in browsertab title