# Generated by Django 2.1 on 2018-09-15 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20180915_2056'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='ClientProfile',
        ),
        migrations.RenameModel(
            old_name='Trainer',
            new_name='TrainerProfile',
        ),
    ]
