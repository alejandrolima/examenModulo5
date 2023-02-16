# Generated by Django 3.1.4 on 2020-12-21 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20201221_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='nivel',
            field=models.CharField(blank=True, choices=[('PRIMARIO', 'Primario'), ('SECUNDARIO', 'Secundario'), ('TERCIARIO', 'Terciario'), ('ESPECIAL', 'Especial')], default='TERCIARIO', max_length=50, null=True, verbose_name='Nivel'),
        ),
    ]
