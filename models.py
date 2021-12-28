from django.db import models

# Create your models here.

class Student (models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    date_of_birth= models.DateField()
    Location= models.CharField(max_length=100)
    contact= models.IntegerField()
    parent = models.CharField(max_length=100)
    class_room = models.ForiegnField(Class_Room, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher)
    class_teacher =models.ForiegnKey(Teacher, on_delete=models.CASCADE)
    disability = models.CharField("disability status", max_length=3, choices=Disabilities)
    illness = models.CharField(max_length=500, blank=True, null=True)
    allergies = models.CharField(max_length=3, choices=Allergies)
    gender = models.CharField(max_length=1, choices=((M,Male),(F,Female),(O,Other)))
    profile_image = models.CharField(max_length=200) 
    prefect = models.CharField(max_length=3, choices=Prefect_Positions)
    parent_confirmation = models.BooleanField(verbose_name="parent confirmation status")
    def __str__():
        return self.first_name + " "+ self.last_name


class Class_Room (models.Model):
    class_name = models.CharField(max_length=30)
    students = models.ManytoManyField(Student)
    class_teacher = models.ForiegnKey(Teacher)
    def _str_():
        return self.class_name
    

class Teacher (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=21)
    date_of_birth = models.DateField()
    location = models.CharField(max_length=100)


