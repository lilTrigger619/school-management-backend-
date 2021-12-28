from django.db import models
from Students.models import Student
from Teachers.models import Staff

# Create your models here.
class ClassRoom (models.Model):
    students = models.ManyToManyField(Student)
    class_teacher = models.OneToOneField(Staff, on_delete=models.CASCADE)
    staff = models.ManyToManyField(Staff)
    name = models.CharField(max_length=40,)
    
    def __str__(self):
        return self.name
