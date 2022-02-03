from django.db import models
from Teachers.models import Staff
from Semester_1.models import Sem_1
from Semester_2.models import Sem_2
from Semester_3.models import Sem_3

# Create your models here.
class Level(models.Model):
    name = models.CharField(max_length=255)
    staff = models.ManyToManyField(Staff)
    sem_1 = models.OneToOneField(Sem_1, on_delete=models.CASCADE)
    sem_2 = models.OneToOneField(Sem_2, on_delete=models.CASCADE)
    sem_3 = models.OneToOneField(Sem_3, on_delete=models.CASCADE)
    #all three sems have one to  one filed to this module
    #level.student_set(so as to remove the student
    #when they have been added to another class).

    def __str__(self):
        return self.name
