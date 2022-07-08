# Generated by Django 2.2.24 on 2022-02-05 20:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_auto_20220205_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefect',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prefect',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Students.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uuid',
            field=models.CharField(default=uuid.UUID('e2056d56-bc2d-41c6-9c6d-ee077dbd6f4c'), max_length=4000),
        ),
    ]