# Generated by Django 4.0.5 on 2022-07-01 18:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0026_alter_staff_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='uuid',
            field=models.CharField(default=uuid.UUID('3f46c123-0678-486a-98dd-953d3306ec5f'), max_length=4000),
        ),
    ]