# Generated by Django 2.2.24 on 2022-02-05 22:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0003_auto_20220205_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='uuid',
            field=models.CharField(default=uuid.UUID('f06d8282-d188-43ed-9d83-9663026c440e'), max_length=4000),
        ),
    ]
