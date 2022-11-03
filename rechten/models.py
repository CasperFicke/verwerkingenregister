from django.db import models

import uuid

# abstracts from django extensions
from django_extensions.db.models import (
  TimeStampedModel,
	ActivatorModel 
)

# Rol model
class Rol(TimeStampedModel, ActivatorModel, models.Model):
  class Meta:
    ordering            = ['naam']
    verbose_name_plural = 'rollen'
  # attributes
  naam         = models.CharField('rol', max_length=100)
  beschrijving = models.TextField('Beschrijving', blank=True)
  # secundair
  uuid         = models.UUIDField(unique=True, default=uuid.uuid4, help_text='Unique identifier (UUID4)')
  
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.naam