# Generated by Django 2.2.24 on 2021-12-26 20:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base_user_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='c_user',
            options={'permissions': [('Modify or add data', 'The user can create or add students')]},
        ),
        migrations.AlterField(
            model_name='c_user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 20, 13, 10, 846741, tzinfo=utc)),
        ),
    ]
