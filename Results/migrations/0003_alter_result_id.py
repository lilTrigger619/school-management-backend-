# Generated by Django 4.0.5 on 2022-06-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Results', '0002_result_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
