# reserveren/models.py

# django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Business model
class Business(models.Model):
  class Meta:
    verbose_name        = 'Bedrijf'
    verbose_name_plural = 'Bedrijven'
  # attributes
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

# Guest model
class Guest(models.Model):
  class Meta:
    verbose_name        = 'Gast'
    verbose_name_plural = 'Gasten'
  # attributes
  first_name = models.CharField(max_length=50)
  last_name  = models.CharField(max_length=50)
  email      = models.EmailField()
  phone      = models.CharField(max_length=12)
  # relaties
  business   = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)

  @property
  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  def __str__(self):
    return self.full_name

# booking model
class Booking(models.Model):
  class Meta:
    verbose_name        = 'Reservering'
    verbose_name_plural = 'Reserveringen'
  class RoomTypes(models.TextChoices):
    SINGLE = "Single"
    DOUBLE = "Double"
    FAMILY = "Family"
  # relaties
  guest            = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='bookings')
  # attributes
  room_type        = models.CharField(max_length=10, choices=RoomTypes.choices)
  date             = models.DateField()
  number_of_nights = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(365)])

  def __str__(self):
    return f"{self.guest.full_name}: {self.number_of_nights} nights in {self.room_type} room"