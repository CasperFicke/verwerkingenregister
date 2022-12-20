# algoritmes/models.py

# django
from django.db import models
from django.urls import reverse
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
)

# Algoritme Model
class Algoritme(
	TimeStampedModel, 
	ActivatorModel,
	Model
	):
  class Meta:
    verbose_name_plural = "Algoritmes"
  # attributes
  naam = models.CharField('algoritme', max_length=200)
  # create absolute url
  def get_absolute_url(self):
    return reverse('algoritmes:show-algoritme', args=[self.id])

  def __str__(self):
    return f'{self.naam}'