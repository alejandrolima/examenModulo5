# Generated by Django 3.1.4 on 2021-01-07 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0033_perfil_sigla'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='etiqueta',
            options={'ordering': ['nombre']},
        ),
    ]
