from django.db import models
from Course.models import Course
from Teachers.models import Staff

# Create your models here.
'''
when a student enters a quiz, a quiz object will be created.
For every quiz question created, there will be a quiz_uuid field
which will be created from the course's quiz question's uuid.

Same for every question in all Quiz set.
    This is to be able to see the score for that particular quiz,
    and also refer to the student's answers for that quiz.
'''

#Main quiz object for quiz
class Quiz_Answer(models.Model):
    title = models.TextField()
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=223)

#objective question model and options
class Obj(models.Model):
    question_uuid = models.CharField(max_length=223)
    quiz = models.ForeignKey(Quiz_Answer, on_delete=models.CASCADE)
    answer = models.CharField(max_length=233, blank=True, null=True)
    std_answer = models.CharField(max_length=223, blank=True, null=True)

#Text_input question and answer.
class Written(models.Model):
    question_uuid = models.CharField(max_length=233)
    answer = models.TextField(blank=True, null=True)
    quiz = models.ForeignKey(Quiz_Answer, on_delete=models.CASCADE)
    student_answer = models.CharField(max_length=233, null=True, blank=True)


#file upload question and answer.
def quiz_answer(instance, filename):
    return 'Student/{0} {1}/quiz_answers/{2}'.format(instance.staff.first_name,
                                                instance.staff.last_name,
                                                filename)

class File_upload(models.Model):
    question_uuid = models.CharField(max_length=223)
    quiz = models.ForeignKey(Quiz_Answer, on_delete=models.CASCADE)
    std_answer = models.FileField(upload_to=quiz_answer, blank=True, null=True)
