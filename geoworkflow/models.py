# geoworkflow/models.py

import uuid

# Django
from django.db import models
from django.urls import reverse

# Gemeente model
class Gemeente(models.Model):
  class Meta:
    ordering            = ['naam']
    verbose_name        = 'gemeente'
    verbose_name_plural = 'gemeenten'
  # attributes
  naam  = models.CharField('gemeentenaam', max_length=100)
  email = models.EmailField('E-mail', max_length=100)
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.naam}'

# Straat model
class Straat(models.Model):
  class Meta:
    ordering            = ['naam']
    verbose_name        = 'straat'
    verbose_name_plural = 'straten'
  # attributes
  naam     = models.CharField('straatnaam', max_length=100)
  # relaties
  gemeente = models.ForeignKey('gemeente', on_delete=models.CASCADE, related_name='straten')
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.naam}'

# BAG-objecttype model
class Bagobjecttype(models.Model):
  class Meta:
    ordering            = ['naam']
    verbose_name        = 'BAG-objecttype'
    verbose_name_plural = 'BAG objecttypen'
  # attributes
  naam     = models.CharField('Bagobjecttype', max_length=100)
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.naam}'

# BAG-gebeurtenis model
class Baggebeurtenis(models.Model):
  class Meta:
    ordering            = ['naam']
    verbose_name        = 'BAG-gebeurtenis'
    verbose_name_plural = 'BAG gebeurtenissen'
  # attributes
  naam          = models.CharField('Baggebeurtenis', max_length=100)
  # relaties
  bagobjecttype = models.ForeignKey('Bagobjecttype', blank=True, null=True, on_delete=models.CASCADE, related_name='baggebeurtenissen')
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.naam}'

# BAG-registratie model
class Bagregistratie(models.Model):
  class Meta:
    ordering            = ['datum_ontvangst']
    verbose_name        = 'BAG-registratie'
    verbose_name_plural = 'BAG registraties'
  # attributes
  lokatieomschrijving = models.CharField('Lokatieomschrijving', blank=True, max_length=250)
  besluit             = models.CharField('besluit', blank=True, max_length=100)
  datum_besluit       = models.DateField('Datum besluit', blank=True, null=True)
  datum_ontvangst     = models.DateField('Datum ontvangst', blank=True, null=True)
  volledig_ontvangen  = models.BooleanField('Volledig ontvangen', default=False)
  juist_aangeleverd   = models.BooleanField('Juist aangeleverd', default=False)
  # relaties
  gemeente            = models.ForeignKey('Gemeente', blank=True, null=True, on_delete=models.CASCADE, related_name='bagregistraties')
  straat              = models.ForeignKey('Straat', blank=True, null=True, on_delete=models.CASCADE, related_name='bagregistraties')
  bagobjecttype       = models.ForeignKey('Bagobjecttype', blank=True, null=True, on_delete=models.CASCADE, related_name='bagregistraties')
  baggebeurtenis      = models.ForeignKey('Baggebeurtenis', blank=True, null=True, on_delete=models.CASCADE, related_name='bagregistraties')
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.besluit}'