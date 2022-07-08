# Generated by Django 4.0.5 on 2022-07-01 18:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0024_alter_staff_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='uuid',
            field=models.CharField(default=uuid.UUID('73658adc-688b-4941-b4b5-9b442565662e'), max_length=4000),
        ),
    ]