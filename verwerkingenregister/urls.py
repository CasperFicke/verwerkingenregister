# verwerkigenregister/urs.py

# django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  # App urls
  path('', include('site_basis.urls', namespace="site-basis")),
  path('', include('users.urls', namespace="users")),
  path('', include('verwerkingen.urls', namespace="verwerkingen")),
  # debug urls
  #path("__debug__", include('debug_toolbar.urls')),
]