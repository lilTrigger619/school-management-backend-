# Generated by Django 2.2.24 on 2022-02-02 21:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0006_auto_20220202_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='uuid',
            field=models.CharField(default=uuid.UUID('7b3e574f-ee80-4fde-8249-f93fa237144f'), max_length=4000),
        ),
    ]