# Generated by Django 2.2.24 on 2022-02-02 13:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_auto_20220202_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='uuid',
            field=models.CharField(default=uuid.UUID('c09b1047-abf0-4fc6-b85a-dc9cbbfab0aa'), max_length=4000),
        ),
    ]