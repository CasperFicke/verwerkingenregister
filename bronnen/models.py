# bronnen/models.py

import uuid

# Django
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from waarmerken.models import Zaakstatus, Zaaktype


# Bron model
class Bron(models.Model):
  naam         = models.CharField('bron-naam', max_length=100)
  beschrijving = models.TextField('beschrijving', max_length=250, blank=True)
  url          = models.URLField('URL (SLD.TLD)', max_length=100)
  class Meta:
    ordering            = ['naam']
    verbose_name_plural = 'bronnen'
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.naam

# Betrokkene model
class Betrokkene(models.Model):
  naam       = models.CharField('betrokkene-naam', max_length=100)
  postcode   = models.CharField('postcode', blank=True, null=True, max_length=10)
  huisnummer = models.IntegerField('huisnummer', blank=True, null=True)
  class Meta:
    ordering            = ['naam']
    verbose_name_plural = 'betrokkenen'
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.naam

# Zaak model
class Zaak(models.Model):
  # relaties
  betrokkene   = models.ForeignKey(Betrokkene, blank=True, null=True, on_delete=models.SET_NULL, default='onbekend', related_name='zaken')
  bron         = models.ForeignKey(Bron, blank=True, null=True, on_delete=models.SET_NULL, related_name='zaken')
  zaaktype     = models.ForeignKey(Zaaktype, blank=True, null=True, on_delete=models.SET_NULL, related_name='zaken')
  status       = models.ForeignKey(Zaakstatus, blank=True, null=True, on_delete=models.SET_NULL, related_name='zaken')
  casemanager  = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='zaken')
  # attributen
  zaakonderwerp = models.CharField('zaakonderwerp', max_length=100)
  class Meta:
    verbose_name_plural = 'zaken'
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.zaakonderwerp

# Zoekvraag model
class Zoekvraag(models.Model):
  # attributen
  naam         = models.CharField('zoekvraag-naam', max_length=100)
  #relaties
  betrokkene   = models.ForeignKey(Betrokkene, blank=True, null=True, on_delete=models.SET_NULL, default='onbekend', related_name='zoekvragen')
  bron         = models.ManyToManyField(Bron, blank=True, related_name='zoekvragen')
  class Meta:
    ordering            = ['naam']
    verbose_name_plural = 'zoekvragen'
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.naam
