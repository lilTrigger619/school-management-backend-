# Generated by Django 2.2.24 on 2022-02-05 22:42

import Std_quiz.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0002_course_staff'),
        ('Teachers', '0004_auto_20220205_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('uuid', models.CharField(max_length=223)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Course')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Teachers.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Written',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_uuid', models.CharField(max_length=233)),
                ('answer', models.TextField(blank=True, null=True)),
                ('student_answer', models.CharField(blank=True, max_length=233, null=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Std_quiz.Quiz_Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Obj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_uuid', models.CharField(max_length=223)),
                ('answer', models.CharField(blank=True, max_length=233, null=True)),
                ('std_answer', models.CharField(blank=True, max_length=223, null=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Std_quiz.Quiz_Answer')),
            ],
        ),
        migrations.CreateModel(
            name='File_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_uuid', models.CharField(max_length=223)),
                ('std_answer', models.FileField(blank=True, null=True, upload_to=Std_quiz.models.quiz_answer)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Std_quiz.Quiz_Answer')),
            ],
        ),
    ]
