# Generated by Django 2.2.24 on 2022-02-05 20:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base_user_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 20, 7, 13, 574057, tzinfo=utc)),
        ),
    ]
