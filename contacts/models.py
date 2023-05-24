# contacts/models.py

from django.db import models

# contact model
class Contact(models.Model):
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=20)

  def __str__(self):
    return self.name