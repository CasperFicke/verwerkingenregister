# utils/abstracts/py

import uuid
from django.db import models

# Voeg een uuid toe aan ieder model dat je maakt op basis van dit abstract
class Model(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)

  class Meta:
    abstract = True