# Generated by Django 2.0.7 on 2018-08-08 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20180808_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='room',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]