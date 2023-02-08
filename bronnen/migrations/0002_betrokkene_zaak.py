# Generated by Django 4.1.2 on 2023-02-08 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waarmerken', '0006_rename_waarmerkniveai_documentwaarmerking_waarmerkniveau'),
        ('bronnen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Betrokkene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=100, verbose_name='bron-naam')),
            ],
            options={
                'verbose_name_plural': 'betrokkenen',
                'ordering': ['naam'],
            },
        ),
        migrations.CreateModel(
            name='Zaak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zaakonderwerp', models.CharField(max_length=100, verbose_name='zaakonderwerp')),
                ('betrokkene', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zaken', to='bronnen.betrokkene')),
                ('bron', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zaken', to='bronnen.bron')),
                ('zaaktype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zaken', to='waarmerken.zaaktype')),
            ],
            options={
                'verbose_name_plural': 'zaken',
            },
        ),
    ]
