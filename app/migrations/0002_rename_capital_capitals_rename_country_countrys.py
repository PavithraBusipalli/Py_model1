# Generated by Django 4.2.7 on 2023-12-08 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Capital',
            new_name='Capitals',
        ),
        migrations.RenameModel(
            old_name='Country',
            new_name='Countrys',
        ),
    ]
