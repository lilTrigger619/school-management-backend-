# Generated by Django 4.0.5 on 2022-06-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_user_manager', '0005_alter_c_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
