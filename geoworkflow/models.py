# geoworkflow/models.py

import uuid

# Django
from django.db import models
from django.urls import reverse

# Gemeente model
class Gemeente(models.Model):
  class Meta:
    ordering = ['naam']
    verbose_name_plural = 'gemeenten'
  # attributes
  naam  = models.CharField('gemeentenaam', max_length=100)
  email = models.EmailField('E-mail', max_length=100)
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.naam} - e-mail: {self.email}'
