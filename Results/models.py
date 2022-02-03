from django.db import models
from Students.models import Student

# Create your models here.
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    level = models.CharField(max_length=222)
    semester = models.CharField(max_length=222)
    course = models.CharField(max_length=222)
    title = models.CharField(max_length=222)
    grade = models.CharField(max_length=222)
    class_score = models.IntegerField()
    exam_score = models.IntegerField()
    mid_sem = models.IntegerField()
    total_credit_hours = models.IntegerField()

    def __str__(self):
        return '{0} semester: {1}'.format(self.student.firstname, self.level)
