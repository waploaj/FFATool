# Generated by Django 3.0.3 on 2020-03-08 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0004_ospospeople'),
        ('Employee', '0003_auto_20200308_1721'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
