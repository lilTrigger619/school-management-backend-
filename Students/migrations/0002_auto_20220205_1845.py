# Generated by Django 2.2.24 on 2022-02-05 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Students', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
      #  migrations.AddField(
      #      model_name='student',
      #      name='user',
      #      field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
      #  ),
      #  migrations.AddField(
      #      model_name='prefect',
      #      name='student',
      #      field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.Student'),
      #  ),
    ]
