# Generated by Django 4.0.5 on 2022-06-23 00:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0017_alter_file_upload_uuid_alter_obj_uuid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='uuid',
            field=models.CharField(default=uuid.UUID('1a4d548a-04fd-4c88-ac1b-32310cd1ce80'), max_length=223),
        ),
        migrations.AlterField(
            model_name='obj',
            name='uuid',
            field=models.CharField(default=uuid.UUID('464d5398-e3f0-446c-86ed-07cd31eb1e5c'), max_length=223),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='uuid',
            field=models.CharField(default=uuid.UUID('eca76392-2c90-43d3-b9d8-457fc9d081fd'), max_length=223),
        ),
        migrations.AlterField(
            model_name='written',
            name='uuid',
            field=models.CharField(default=uuid.UUID('f76016b0-a006-42bb-b874-5ef067249a0a'), max_length=223),
        ),
    ]
