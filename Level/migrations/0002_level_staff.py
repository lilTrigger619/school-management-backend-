# Generated by Django 2.2.24 on 2022-02-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Level', '0001_initial'),
        ('Teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='staff',
            field=models.ManyToManyField(to='Teachers.Staff'),
        ),
    ]
