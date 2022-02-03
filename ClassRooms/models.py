from django.db import models
from Teachers.models import Staff
from Semester_1.models import Sem_1
from Semester_2.models import Sem_2
from Semester_3.models import Sem_3

#to-do semester which will hold the fees.
#this module will not be used to access student class
#rather, it will be used to access all the previous
#student data from  previous classRooms.

# Create your models here.
class Class_list (models.Model):
    name = models.CharField(max_length=40,)
    sem_1 = models.OneToOneField(Sem_1, on_delete=models.CASCADE)
    sem_2 = models.OneToOneField(Sem_2, on_delete=models.CASCADE)
    sem_3 = models.OneToOneField(Sem_3, on_delete=models.CASCADE)
    staff = models.ManyToManyField(Staff)
    
    def __str__(self):
        return self.name
