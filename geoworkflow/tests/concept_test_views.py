# geoworkflow/tests/test_views.py

# django
from django.test import TestCase, Client
from django.urls import reverse

# local
from geoworkflow.models import Termijn, Gemeente, Bagobjecttype, Bagregistratie, Status, Bagregistratie

import json

# Tests
class TestViews(TestCase):

  # setup
  def setUp(self):
    self.client    = Client()
    self.index_url = reverse('geoworkflow:index')
    self.bagregistraties_url     = reverse('geoworkflow:all-bagregistraties')
    self.show_bagregistratie_url = reverse('geoworkflow:show-bagregistratie', args=['some_id'])

  # geoworkflow-index view
  def test_index_GET(self):
    response = self.client.get(self.index_url)
    # assertions (tests)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'geoworkflow/index.html')

  # all-bagregistraties view
  def test_bagregistraties_GET(self):
    response = self.client.get(self.bagregistraties_url)
    # assertions (tests)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'geoworkflow/all_bagregistraties.html')

  # show-bagregistratie view
  def test_show_bagregistratie_GET(self):
    response = self.client.get(self.show_bagregistratie_url)
    # assertions (tests)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'geoworkflow/bagregistraties.html')
