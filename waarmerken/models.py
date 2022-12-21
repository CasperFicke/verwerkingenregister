# waarmerken/models.py

# django
from django.db import models
from django.urls import reverse
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
)

# Zaaktype Model
class Zaaktype(
	TimeStampedModel, 
	ActivatorModel,
	Model
	):
  class Meta:
    verbose_name_plural = "Zaaktypen"
  # attributes
  naam = models.CharField('zaaktype', max_length=200)
  # create absolute url
  def get_absolute_url(self):
    return reverse('waarmerken:show-zaaktype', args=[self.id])

  def __str__(self):
    return f'{self.naam}'

# Documenttype Model
class Documenttype(
	TimeStampedModel, 
	ActivatorModel,
	Model
	):
  class Meta:
    verbose_name_plural = "Documenttypen"
  # attributes
  naam = models.CharField('documenttype', max_length=200)
  # create absolute url
  def get_absolute_url(self):
    return reverse('waarmerken:show-documenttype', args=[self.id])

  def __str__(self):
    return f'{self.naam}'

# Waarmerkniveau Model
class Waarmerkniveau(
	TimeStampedModel, 
	ActivatorModel,
	Model
	):
  class Meta:
    verbose_name_plural = "Waarmerkniveaus"
  # attributes
  naam = models.CharField('waarmerkniveau', max_length=200)

  def __str__(self):
    return f'{self.naam}'

# Documentwaarmerking
class Documentwaarmerking(
	TimeStampedModel, 
	ActivatorModel,
	Model
	):
  '''
  waarmerken.Documentwaarmerking
  Stores a single documentwaarmerking entry related to :model:`waarmerken.Zaaktype`,
  :model:`waarmerken.Document` and :model:`waarmerken.Waarmerkniveau`.
  '''
  class Meta:
    verbose_name_plural = "Document waarmerkingen"
  # relaties
  zaaktype       = models.ForeignKey(Zaaktype, null=True, on_delete=models.CASCADE)
  documenttype   = models.ForeignKey(Documenttype, null=True, on_delete=models.CASCADE)
  waarmerkniveau = models.ForeignKey(Waarmerkniveau, null=True, on_delete=models.CASCADE)
