# Generated by Django 2.2.24 on 2022-02-02 20:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base_user_manager', '0002_auto_20220202_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 20, 11, 40, 608535, tzinfo=utc)),
        ),
    ]