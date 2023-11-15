# geoworkflow/models.py

import uuid

# Django
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# abstracts from django extensions
from django_extensions.db.models import (
  TimeStampedModel,
	ActivatorModel 
)

from datetime import date, timedelta

# Termijn model
class Termijn(models.Model):
  class Meta:
    ordering            = ['naam']
    verbose_name        = 'Termijn'
    verbose_name_plural = 'Termijnen'
  # attributes
  naam    = models.CharField('termijnnaam', max_length=100)
  termijn = models.IntegerField('termijn in dagen', blank=True, null=True, default=0)
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.naam} - {self.termijn} dagen'

# Gemeente model
class Gemeente(models.Model):
  class Meta:
    ordering            = ['naam']
    verbose_name        = 'gemeente'
    verbose_name_plural = 'gemeenten'
    constraints         = [models.UniqueConstraint(fields=['naam', 'email'], name='unique gemeente')]
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
    constraints         = [models.UniqueConstraint(fields=['naam', 'gemeente'], name='unique straat')]
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

# Status model
class Status(models.Model):
  class Meta:
    verbose_name        = 'Status'
    verbose_name_plural = 'Statussen'
  class RegistratieTypes(models.TextChoices):
    BAG = "BAG administratie"
    WOZ = "WOZ administratie"
    GEO = "GEO administratie"
  # attributes
  naam        = models.CharField(max_length=100)
  registratie = models.CharField(max_length=100, choices=RegistratieTypes.choices)

  def __str__(self):
    return f"{self.registratie}: {self.naam}"
  
# BAG-registratie model
class Bagregistratie(models.Model):
  class Meta:
    ordering            = ['datum_ontvangst']
    verbose_name        = 'BAG-registratie'
    verbose_name_plural = 'BAG registraties'
    #constraints         = [models.CheckConstraint(check=Q(age__gte=18), name='age_gte_18')]
  class TariefTypes(models.TextChoices):
    HOOG = "hoog"
    LAAG = "laag"
    NVT  = "n.v.t."
  name_regex = RegexValidator(
    regex   = r'^[a-zA-Z, 0-9]+$',
    message = "Gebruik alleen letters en cijfers. Geen speciale karakters"
  )
  # attributes
  lokatieomschrijving = models.CharField('Lokatieomschrijving', validators=[name_regex], blank=True, max_length=250)
  huisnummer          = models.CharField('Huisnummer', validators=[name_regex], blank=True, max_length=20)
  besluit             = models.CharField('besluit', validators=[name_regex], blank=True, max_length=100)
  datum_besluit       = models.DateField('Datum besluit', blank=True, null=True)
  datum_ontvangst     = models.DateField('Datum ontvangst', blank=True, null=True)
  volledig_ontvangen  = models.BooleanField('Volledig ontvangen', default=False)
  juist_aangeleverd   = models.BooleanField('Juist aangeleverd', default=False)
  tarief              = models.CharField(max_length=50, choices=TariefTypes.choices, default='NVT')
  # relaties
  author              = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='bagregistraties')
  gemeente            = models.ForeignKey('Gemeente', blank=True, null=True, on_delete=models.CASCADE, related_name='bagregistraties')
  straat              = models.ForeignKey('Straat', blank=True, null=True, on_delete=models.CASCADE, related_name='bagregistraties')
  bagobjecttype       = models.ForeignKey('Bagobjecttype', blank=True, null=True, on_delete=models.CASCADE, related_name='bagregistraties')
  baggebeurtenis      = models.ForeignKey('Baggebeurtenis', blank=True, null=True, on_delete=models.CASCADE, related_name='bagregistraties')
  status              = models.ForeignKey('Status', blank=True, null=True, on_delete=models.CASCADE, related_name='bagregistraties')
  
  # method om te bepalen of bagregistratie nog geldig is
  @property
  def valid(self):
    today    = date.today()
    if self.datum_ontvangst < today:
      valid = False
    else:
      valid = True
    return valid
  
  # method om te bepalen of bagregistratie op tijd verwerkt is
  @property
  def optijdverwerkt(self):
    maxverwerkt  = date.today()
    if self.datum_ontvangst < maxverwerkt:
      valid = False
    else:
      valid = True
    return valid
  
  # method to calculate number of days left to verwerk bagregistratie
  @property
  def days_till_eindeverwerkingstijd(self):
    today    = date.today()
    if self.datum_ontvangst == today:
      num_days_stripped = 0
    else:
      num_days = today - self.datum_ontvangst
      num_days_stripped = int(str(num_days).split(' ', 1)[0])
    print('aantal dagen sinds ontvangst:', num_days_stripped)
    termijn  = Termijn.objects.get(naam='BAG - Maximale verwerkingstermijn')
    end_date = self.datum_ontvangst + timedelta(days=termijn.termijn)
    #einddatum = today + timedelta(days=termijn)
    print('termijn:', termijn.termijn)
    print('einddatum:',  end_date)
    #num_days_stripped = int(str(num_days).split(' ', 1)[0]) + termijn.termijn
    print(num_days_stripped)
    if num_days_stripped > termijn.termijn:
      return num_days_stripped
    elif num_days_stripped == 0:
      return 'vandaag'
    else:
      return f"{num_days_stripped} dagen te laat"
  
  # create absolute url
  def get_absolute_url(self):
    return reverse('geoworkflow:show-bagregistratie', args=[self.id])
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.besluit}'

# NotitieType model
class NotitieType(TimeStampedModel,ActivatorModel,models.Model):
  class Meta:
    ordering            = ['type']
    verbose_name        = 'notitie-type'
    verbose_name_plural = 'notitie types'
  # attributes
  type         = models.CharField('Notitie Type', max_length=100)
  beschrijving = models.TextField('Beschrijving', blank=True)
  # secundair
  uuid         = models.UUIDField(unique=True, default=uuid.uuid4, help_text='Unique identifier (UUID4)')
  
  # functie om model in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.type

# Notitie Model
class Notitie (models.Model):
  title      = models.CharField(max_length=255)
  body       = models.TextField(max_length=300)
  date_added = models.DateTimeField(auto_now_add=True)
  # relaties
  type           = models.ForeignKey(NotitieType, blank=True, null=True, on_delete=models.SET_NULL, related_name='notities')
  bagregistratie = models.ForeignKey(Bagregistratie, on_delete=models.CASCADE, related_name="notities")
  author         = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='notities')

  # functie om in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return f'{self.title}' 