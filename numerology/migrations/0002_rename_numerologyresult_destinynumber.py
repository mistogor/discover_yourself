# Generated by Django 4.1.6 on 2023-02-28 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('numerology', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NumerologyResult',
            new_name='DestinyNumber',
        ),
    ]