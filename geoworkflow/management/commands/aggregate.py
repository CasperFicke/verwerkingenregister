# geoworkflow/management/commands/aggregate.py

# django
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

# local
from geoworkflow.models import Bagregistratie
from easyaudit.models import CRUDEvent

class Command(BaseCommand):
  help = 'aggregate CRUD-events'

  def handle(self, *args, **kwargs):
    bagregistratie = Bagregistratie.objects.first()
    content_type   = ContentType.objects.get_for_model(bagregistratie)
    # 
    crud_events    = CRUDEvent.objects.filter(
      content_type = content_type,
      object_id    = bagregistratie.pk
    ).order_by('datetime')
    #
    for event in crud_events:
      print (event.changed_fields)
