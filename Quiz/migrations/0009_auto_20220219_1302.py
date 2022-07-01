# Generated by Django 3.2.12 on 2022-02-19 13:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0008_auto_20220208_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='uuid',
            field=models.CharField(default=uuid.UUID('521e748f-f7b4-48dd-a450-625fd56d159b'), max_length=223),
        ),
        migrations.AlterField(
            model_name='obj',
            name='uuid',
            field=models.CharField(default=uuid.UUID('e844495a-fefc-42bb-9a35-b172952ee184'), max_length=223),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='uuid',
            field=models.CharField(default=uuid.UUID('caca4b46-e7c5-474a-84d7-4a4a0b674632'), max_length=223),
        ),
        migrations.AlterField(
            model_name='written',
            name='uuid',
            field=models.CharField(default=uuid.UUID('92eefc67-a5d5-44af-aefb-30f0d8b02bde'), max_length=223),
        ),
    ]