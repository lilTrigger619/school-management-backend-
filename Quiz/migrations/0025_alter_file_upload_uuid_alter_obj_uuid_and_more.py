# Generated by Django 4.0.5 on 2022-07-01 18:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0024_alter_file_upload_uuid_alter_obj_uuid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='uuid',
            field=models.CharField(default=uuid.UUID('20d8639a-113e-4226-8367-4186917536c1'), max_length=223),
        ),
        migrations.AlterField(
            model_name='obj',
            name='uuid',
            field=models.CharField(default=uuid.UUID('3a8dc8c8-b50f-4e0c-804d-2442863c8df8'), max_length=223),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='uuid',
            field=models.CharField(default=uuid.UUID('52aaa836-b138-40ea-a8b2-4b0bc3fda6fd'), max_length=223),
        ),
        migrations.AlterField(
            model_name='written',
            name='uuid',
            field=models.CharField(default=uuid.UUID('22f9537e-b3e8-4cbb-96e5-926bb46d20bd'), max_length=223),
        ),
    ]