# Generated by Django 3.1.4 on 2020-12-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20201223_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='lead',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Lead'),
        ),
    ]
