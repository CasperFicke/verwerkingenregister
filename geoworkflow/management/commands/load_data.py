# geoworkflow/management/commands/load_data.py

# django
from django.core.management.base import BaseCommand

# local
from geoworkflow.models import Bagobjecttype, Baggebeurtenis

# load command
class Command(BaseCommand):
    help = 'Load Bagobjecttypen en Bag gebeurtenissen'

    def handle(self, *args, **kwargs):
        Baggebeurtenis.objects.all().delete()
        bagobjecttype_names = [
            'Computer Science', 'Mathematics', 'Physics', 'Film Studies'
        ]

        if not Bagobjecttype.objects.count():
            for bagobjecttype_name in bagobjecttype_names:
                Bagobjecttype.objects.create(name=bagobjecttype_name)

        # Computer Science
        cs = Bagobjecttype.objects.get(name='Computer Science')

        compsci_baggebeurtenissen = [
            'AI',
            'Machine Learning',
            'Web Development',
            'Software Engineering', 
            'NoSQL Databases'
        ]

        for baggebeurtenis in compsci_baggebeurtenissen:
            Baggebeurtenis.objects.create(name=baggebeurtenis, bagobjecttype=cs)

        # Maths
        math = Bagobjecttype.objects.get(name='Mathematics')
        math_baggebeurtenissen = [
            'Linear Algebra',
            'Differential Equations',
            'Graph Theory',
            'Topology',
            'Number Theory'
        ]

        for baggebeurtenis in math_baggebeurtenissen:
            Baggebeurtenis.objects.create(name=module, bagobjecttype=math)

        # PHYSICS
        physics = Bagobjecttype.objects.get(name='Physics')
        physics_baggebeurtenissen = [
            'Quantum Mechanics',
            'Optics',
            'Astronomy',
            'Solid State Physics',
            'Electromagnetic Theory'
        ] 
        for module in physics_baggebeurtenissen:
            Baggebeurtenis.objects.create(name=module, bagobjecttype=physics)

        # Film
        film = Bagobjecttype.objects.get(name='Film Studies')

        film_baggebeurtenissen = [
            'Film Noir',
            'Silent Cinema',
            'American Independent Cinema',
            'Avant-Garde Cinema',
            'Scriptwriting'
        ]

        for module in film_baggebeurtenissen:
            Baggebeurtenis.objects.create(name=module, bagobjecttype=film)