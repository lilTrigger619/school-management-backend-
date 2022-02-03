# Generated by Django 2.2.24 on 2022-02-02 13:40

import Students.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Level', '0001_initial'),
        ('ClassRooms', '0001_initial'),
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male_partner', models.CharField(blank=True, max_length=20, null=True)),
                ('female_partner', models.CharField(blank=True, max_length=30, null=True)),
                ('male_tel_number', models.CharField(blank=True, max_length=30, null=True)),
                ('female_tel_number', models.CharField(blank=True, max_length=30, null=True)),
                ('male_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('female_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Together', 'Together'), ('Married', 'Married'), ('Splitted', 'Splitted'), ('Divorced', 'Divorced'), ('Deceased_partner', 'Deceased_partner')], max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prefect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=223, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('uuid', models.CharField(default=uuid.UUID('c39b3dfa-2780-4b4b-917e-6ac8c78d9a99'), max_length=4000)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('disability', models.CharField(blank=True, max_length=400, null=True)),
                ('illness', models.CharField(blank=True, max_length=500, null=True)),
                ('allergies', models.CharField(blank=True, max_length=410, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=Students.models.photo_upload)),
                ('rep', models.BooleanField(default=False)),
                ('parent_confirmation', models.BooleanField(blank=True, null=True, verbose_name='parent confirmation status')),
                ('Level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Level.Level')),
                ('classroom', models.ManyToManyField(to='ClassRooms.Class_list')),
                ('course', models.ManyToManyField(to='Course.Course')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Students.Parent')),
            ],
        ),
    ]
