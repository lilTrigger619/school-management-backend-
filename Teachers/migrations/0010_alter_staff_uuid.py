# Generated by Django 3.2.12 on 2022-02-19 17:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0009_alter_staff_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='uuid',
            field=models.CharField(default=uuid.UUID('81b5388e-6715-4d15-899e-47924495e731'), max_length=4000),
        ),
    ]