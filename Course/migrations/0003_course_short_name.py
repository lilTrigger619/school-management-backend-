# Generated by Django 3.2.12 on 2022-03-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_course_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='short_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]