# Generated by Django 2.2.24 on 2022-02-02 13:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0002_staff_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='uuid',
            field=models.CharField(default=uuid.UUID('bb9e7b2e-fa32-44a3-aef9-815035fe9709'), max_length=4000),
        ),
    ]