# Generated by Django 4.1.2 on 2023-09-05 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geoworkflow', '0008_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bagregistratie',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bagregistraties', to='geoworkflow.status'),
        ),
    ]
