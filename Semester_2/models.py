from django.db import models
from Course.models import Course


# Create your models here.
class Sem_2(models.Model):
    course = models.ManyToManyField(Course)
    #fees = models.ManyToManyField(Fees)
    def __str__(self):
        return self.level.name;
