# Generated by Django 2.1 on 2018-09-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_auto_20180915_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerprofile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trainerprofile',
            name='location',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='trainerprofile',
            name='skills',
            field=models.CharField(max_length=30, null=True),
        ),
    ]