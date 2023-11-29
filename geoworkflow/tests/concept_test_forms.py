# geoworkflow/tests/test_forms.py

# django
from django.test import SimpleTestCase

# local
from geoworkflow.forms import BagregistratieForm, NotitieForm

# Tests
class TestForms(SimpleTestCase):
  # setup
  def setUp():
    pass
  def test_bagregistratieform_with_valid_data(self):
    form = BagregistratieForm(data={
      'gemeente'           : 'Gemeente',
      'straat'             : 'straat',
      'huisnummer'         : 'huisnummer',
      'bagobjecttype'      : 'bagobjecttype',
      'baggebeurtenis'     : 'baggebeurtenis',
      'besluit'            : 'besluit',
      'datum_besluit'      : 'datum besluit',
      'datum_ontvangst'    : 'datum ontvangst',
      'volledig_ontvangen' : True,
      'juist_aangeleverd'  : True,
      'tarief'             : 'tarief'
    })
    # assertions
    self.assertTrue(form.is_valid())
  
  def test_bagregistratieform_with_no_data(self):
    form = BagregistratieForm(data={})
    # assertions
    self.assertFalse(form.is_valid())
    self.assertEquals(len(form.errors), 3)