# rechten/models.py

# django
from django.db import models
from django.urls import reverse

import uuid

# abstracts from django extensions
from django_extensions.db.models import (
  TimeStampedModel,
	ActivatorModel 
)

# Verwerkingattribuut mverwerkingattribuutodel
class Verwerkingattribuut(TimeStampedModel, ActivatorModel, models.Model):
  class Meta:
    ordering            = ['naam']
    verbose_name_plural = 'verwerkingsattributes'
  # attributes
  naam         = models.CharField('', max_length=100)
  beschrijving = models.TextField('Beschrijving', blank=True)
  # secundair
  uuid         = models.UUIDField(unique=True, default=uuid.uuid4, help_text='Unique identifier (UUID4)')
  
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.naam

# Rol model
# Alle verschillende raadpleeg rollen van het register. voor iedere rol worden de te presenteren attributen in de attribuutlijst opgenomen
class Rol(TimeStampedModel, ActivatorModel, models.Model):
  class Meta:
    ordering            = ['naam']
    verbose_name_plural = 'rollen'
  # attributes
  naam         = models.CharField('rol', max_length=100)
  beschrijving = models.TextField('Beschrijving', blank=True)
  # relaties
  attributes   = models.ManyToManyField(Verwerkingattribuut, blank=True, related_name='rollen') 
  # secundair
  uuid         = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, help_text='Unique identifier (UUID4)')
  
  # create absolute url
  def get_absolute_url(self):
    return reverse('rechten:show-rol', args=[self.uuid])

  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.naam
