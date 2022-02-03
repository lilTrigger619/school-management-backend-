from django.db import models
from django.utils import timezone
from django.conf import settings
from uuid import uuid4
from Level.models import Level
from ClassRooms.models import Class_list
from Course.models import Course
# Create your models here.

# is used to store the image file according to user's id with the file name.
def photo_upload(instance, filename):
    return 'Student/{0} {1}/profile_image/{2}'.format(instance.first_name, instance.last_name, filename)


class Parent (models.Model):
    #parent can have more than one student
    Marrital_status = (
        ('Single', 'Single'),
        ('Together', 'Together'),
        ('Married', 'Married'),
        ('Splitted', 'Splitted'),
        ('Divorced', 'Divorced'),
        ('Deceased_partner', 'Deceased_partner'),
            )

    male_partner = models.CharField(max_length=20, blank=True, null=True)
    female_partner = models.CharField(max_length=30, blank=True, null=True)
    male_tel_number = models.CharField(max_length=30, blank=True, null=True)
    female_tel_number = models.CharField(max_length=30, blank=True, null=True)
    male_email = models.EmailField(null=True, blank=True)
    female_email = models.EmailField(null=True, blank=True)
    marital_status = models.CharField(max_length=15, blank=True, null=True, choices=Marrital_status)


class Student(models.Model):
    Male = 'male'
    Female = 'female'
    Gender = (
        (Male, 'Male'),
        (Female, 'Female'),
            )

    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=223, null=True, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    uuid = models.CharField(max_length=4000, default=uuid4())
    date_of_birth = models.DateField(blank=True, null=True,auto_now_add=False, auto_now=False)
    location = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    #class_room = models.ForeignKey("Class_Room", on_delete=models.CASCADE)
    #teachers = models.ManyToManyField("Teacher")
    #class_teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    disability = models.CharField(max_length=400,   null=True, blank=True)
    illness = models.CharField(max_length=500,null=True, blank=True)
    allergies = models.CharField(max_length=410, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender)
    profile_image = models.ImageField(upload_to=photo_upload, blank=True, null=True)
    rep = models.BooleanField(default=False)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, blank=True, null=True) #Student has only one parent but parent can
    #have more than one student
    parent_confirmation = models.BooleanField(verbose_name="parent confirmation status", blank=True, null=True)
    classroom = models.ManyToManyField(Class_list)
    level = models.ForeignKey(Level , on_delete=models.CASCADE, null=True, blank=True)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.first_name


class Prefect(models.Model):
    name = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
