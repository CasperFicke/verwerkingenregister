# Generated by Django 4.1.2 on 2022-11-08 10:12

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rechten', '0011_remove_verwerkingattribuut_publiceren'),
    ]

    operations = [
        migrations.CreateModel(
            name='PubliceerAttribuut',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unique identifier (UUID4)', primary_key=True, serialize=False, unique=True)),
                ('attribuut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publiceren', to='rechten.verwerkingattribuut')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publiceren', to='rechten.rol')),
            ],
            options={
                'verbose_name_plural': 'publiceer attributes',
            },
        ),
    ]