from django.db import models
from Course.models import Course
from Teachers.models import Staff
import uuid

# Create your models here.


#Main quiz object for quiz
class Quiz(models.Model):
    title = models.TextField()
    uuid = models.CharField(max_length=223, default=uuid.uuid4())
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructions = models.TextField(blank=True, null=True)
    is_obj = models.BooleanField(default=False)
    is_text = models.BooleanField(default=True)
    is_filed = models.BooleanField(default=False)
    due_date = models.IntegerField(null=True, blank=True)
    timer = models.IntegerField(null=True, blank=True)
    radomize_questions = models.BooleanField(default=False)
    radomize_options = models.BooleanField(default=False)

    def __str__(self):
        return self.title


#objective question model and options
class Obj(models.Model):
    question_number = models.IntegerField()
    question = models.TextField()
    uuid = models.CharField(max_length=223, default=uuid.uuid4())
    answer = models.CharField(max_length=223, blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Options(models.Model):
    question = models.ForeignKey(Obj, on_delete=models.CASCADE)
    option = models.CharField(max_length=223)
    option_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.option


#Text_input question and answer.
class Written(models.Model):
    question_number = models.IntegerField(blank=True, null=True)
    question = models.TextField()
    uuid = models.CharField(max_length=223, default=uuid.uuid4())
    answer = models.TextField(blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


#file upload question and answer.
def quiz_file(instance, filename):
    return 'Staff/{0} {1}/quiz_file/{2}'.format(instance.staff.first_name,
                                                instance.staff.last_name,
                                                filename)


class File_upload(models.Model):
    question_text = models.CharField(max_length=255, blank=True, null=True)
    question_file = models.FileField(upload_to=quiz_file,
                                     blank=True,
                                     null=True)
    uuid = models.CharField(max_length=223, default=uuid.uuid4())
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
