# Generated by Django 4.0.5 on 2022-06-19 12:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0014_auto_20220404_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='file_upload',
            name='uuid',
            field=models.CharField(default=uuid.UUID('564eab21-738f-4d4a-91c0-ae03d8b3909c'), max_length=223),
        ),
        migrations.AlterField(
            model_name='obj',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='obj',
            name='uuid',
            field=models.CharField(default=uuid.UUID('47b60b15-c9fb-4656-aa64-45651972a70b'), max_length=223),
        ),
        migrations.AlterField(
            model_name='options',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='uuid',
            field=models.CharField(default=uuid.UUID('b36ee936-9853-47cc-9a3e-fc86245c4fa2'), max_length=223),
        ),
        migrations.AlterField(
            model_name='written',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='written',
            name='uuid',
            field=models.CharField(default=uuid.UUID('cb411ee8-c9a9-4ead-b755-cd1036174487'), max_length=223),
        ),
    ]
