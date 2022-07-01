# Generated by Django 2.2.24 on 2022-02-05 20:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_auto_20220205_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='uuid',
            field=models.CharField(default=uuid.UUID('dd45b2ec-a752-4ed4-bc2c-c4d3f8dc2f54'), max_length=223),
        ),
        migrations.AlterField(
            model_name='obj',
            name='uuid',
            field=models.CharField(default=uuid.UUID('3cf49157-a94a-479e-a6a5-4bcd30e3b215'), max_length=223),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='uuid',
            field=models.CharField(default=uuid.UUID('d3b0f4dd-47a8-4bd4-a39e-6a5d29a51e4f'), max_length=223),
        ),
        migrations.AlterField(
            model_name='written',
            name='uuid',
            field=models.CharField(default=uuid.UUID('74db473e-eb2d-4ac7-a450-f07ed476bc43'), max_length=223),
        ),
    ]
