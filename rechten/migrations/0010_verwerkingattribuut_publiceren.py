# Generated by Django 4.1.2 on 2022-11-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rechten', '0009_rename_attributesa_rol_attributes'),
    ]

    operations = [
        migrations.AddField(
            model_name='verwerkingattribuut',
            name='publiceren',
            field=models.BooleanField(default=False),
        ),
    ]
