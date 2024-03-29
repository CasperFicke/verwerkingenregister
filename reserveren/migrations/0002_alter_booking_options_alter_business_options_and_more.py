# Generated by Django 4.1.2 on 2023-09-04 11:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserveren', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Reservering', 'verbose_name_plural': 'Reserveringen'},
        ),
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': 'Bedrijf', 'verbose_name_plural': 'Bedrijven'},
        ),
        migrations.AlterModelOptions(
            name='guest',
            options={'verbose_name': 'Gast', 'verbose_name_plural': 'Gasten'},
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_nights',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(365)]),
        ),
    ]
