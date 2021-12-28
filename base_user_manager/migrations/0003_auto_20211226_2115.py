# Generated by Django 2.2.24 on 2021-12-26 21:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('base_user_manager', '0002_auto_20211226_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='c_user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='c_user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 21, 15, 10, 395420, tzinfo=utc)),
        ),
    ]
