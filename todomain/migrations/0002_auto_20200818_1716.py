# Generated by Django 3.1 on 2020-08-18 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todomain', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoItems',
            new_name='TodoItem',
        ),
    ]
