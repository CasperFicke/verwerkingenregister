# verwerkigenregister/urls.py

# django
from django.contrib import admin
from django.urls import path, include

# Serve images in development. NOT TO USE IN PRODUCTION
from django.conf import settings
from django.conf.urls.static import static

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
  path('', include('contacts.urls'    , namespace="contacts")),
  # debug urls
  #path("__debug__", include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # DEVELOPMENT ONLY

# Configure Admin area Titles
admin.site.site_header = "Registers Administration"      # header op admin pagina (blauwe balk)
admin.site.index_title = "Site Admin" # koptekst op admin pagina en 1e deel in browsertab title
admin.site.site_title  = "Registers"  # toevoeging (2e deel) in browsertab title