# Generated by Django 4.0.5 on 2022-07-01 18:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0027_alter_student_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='uuid',
            field=models.CharField(default=uuid.UUID('87d6a086-f6a6-40f3-8bcc-555a3e9feb96'), max_length=4000),
        ),
    ]
