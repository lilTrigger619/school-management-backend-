# Generated by Django 2.2.24 on 2022-02-08 08:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0007_auto_20220207_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='uuid',
            field=models.CharField(default=uuid.UUID('4a88ee9f-6df2-4324-9851-36375f3ed64c'), max_length=223),
        ),
        migrations.AlterField(
            model_name='obj',
            name='uuid',
            field=models.CharField(default=uuid.UUID('83354f31-0a16-48a2-8ff5-79926f8cee20'), max_length=223),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='uuid',
            field=models.CharField(default=uuid.UUID('d762103a-7825-4e3a-9eb1-bedb8f6c5a79'), max_length=223),
        ),
        migrations.AlterField(
            model_name='written',
            name='uuid',
            field=models.CharField(default=uuid.UUID('408e6209-f83e-4cac-af85-2c211982cc77'), max_length=223),
        ),
    ]