from django.db import models
from Teachers.models import Staff

#from Semetser_1.models import Sem_1
#from Semester_2.models import Sem_2
#from Semester_3.models import Sem_3


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=223)
    short_name = models.CharField(max_length=10, null=True, blank=True)
    staff = models.ManyToManyField(Staff)

    #all three sems have one to one field to this module
    #course.students_set(already declared).

    def __str__(self):
        return self.name
