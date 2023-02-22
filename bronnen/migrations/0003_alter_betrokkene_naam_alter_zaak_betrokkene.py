# Generated by Django 4.1.2 on 2023-02-13 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bronnen', '0002_betrokkene_zaak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betrokkene',
            name='naam',
            field=models.CharField(max_length=100, verbose_name='betrokkene-naam'),
        ),
        migrations.AlterField(
            model_name='zaak',
            name='betrokkene',
            field=models.ForeignKey(blank=True, default='onbekend', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zaken', to='bronnen.betrokkene'),
        ),
    ]