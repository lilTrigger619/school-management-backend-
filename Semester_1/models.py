from django.db import models
from django.db import models
from Course.models import Course

# Create your models here.
class Sem_1(models.Model):
    course = models.ManyToManyField(Course)
    #Class_list.sem_1
    #fees = models.ManyToManyField(Fees)

    def __str__(self):
        return self.level.name;
