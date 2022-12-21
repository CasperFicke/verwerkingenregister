# verwerkigenregister/urls.py

# django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  # App urls
  path('', include('site_basis.urls', namespace="site-basis")),
  path('', include('users.urls', namespace="users")),
  path('', include('rechten.urls', namespace="rechten")),
  path('', include('verwerkingen.urls', namespace="verwerkingen")),
  path('', include('algoritmes.urls', namespace="algoritmes")),
  path('', include('waarmerken.urls', namespace="waarmerken")),
  # debug urls
  #path("__debug__", include('debug_toolbar.urls')),
]
