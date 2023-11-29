# geoworkflow/tests/test_urls.py

# django
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# local
from geoworkflow.views import indexView, bagregistraties, show_bagregistratie, add_bagregistratie

# Tests
class TestUrls(SimpleTestCase):

   # index geoworkflow url
  def test_index_url_resolves(self):
    url = reverse('geoworkflow:index')
    #print (resolve(url))
    self.assertEquals(resolve(url).func.view_class , indexView)

  # all-bagregistraties url
  def test_bagregistraties_url_resolves(self):
    url = reverse('geoworkflow:all-bagregistraties')
    #print (resolve(url))
    self.assertEquals(resolve(url).func , bagregistraties)

  # show-bagregistratie url
  def test_show_bagregistratie_url_resolves(self):
    url = reverse('geoworkflow:show-bagregistratie', args=['some_id'])
    #print (resolve(url))
    self.assertEquals(resolve(url).func , show_bagregistratie)
    
  # add-bagregistratie url
  def test_add_bagregistratie_url_resolves(self):
    url = reverse('geoworkflow:add-bagregistratie')
    #print (resolve(url))
    self.assertEquals(resolve(url).func , add_bagregistratie)