# geoworkflow/tests/test_models.py

# django
from django.test import TestCase

# local
from geoworkflow.models import Gemeente

# Create your tests here.
class TestModels(TestCase):
  def setUp(self):
    self.gemeente1 = Gemeente.objects.create(
      naam = 'gemeentenummer1',
      email = 'test@test.test'
    )

  def test_gemeente_is_created(self):
    self.assertEquals(self.gemeente1.naam, 'gemeentenummer1')