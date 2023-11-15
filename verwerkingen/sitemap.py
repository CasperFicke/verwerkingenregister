# verwerkingen/sitemap.py

# django
from django.contrib.sitemaps import Sitemap

# local
from .models import Verwerking, Verwerker

# Verwerkingen sitemap
class VerwerkingSitemap(Sitemap):
  changefreq = 'weekly'
  priority   = 0.9

  def items(self):
    return Verwerking.objects.all()
  def lastmod(self, obj):
    return obj.created

# Verwerkers sitemap
class VerwerkerSitemap(Sitemap):
  changefreq = 'weekly'
  priority   = 0.9

  def items(self):
    return Verwerker.objects.all()
  def lastmod(self, obj):
    return obj.created
