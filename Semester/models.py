from django.db import models
from Course.models import Course

# Create your models here.

class Sem(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    course = models.ManyToManyField(Course)
    #level_set
    #Result_set
    #Fees_set
    #Course_set

    def __str__(self):
        return self.name
