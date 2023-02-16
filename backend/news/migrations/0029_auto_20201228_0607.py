# Generated by Django 3.1.4 on 2020-12-28 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0028_auto_20201228_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corresponsal',
            name='tipo',
        ),
        migrations.AddField(
            model_name='corresponsal',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corresponsales', to='news.perfil', verbose_name='Tipo'),
        ),
    ]
