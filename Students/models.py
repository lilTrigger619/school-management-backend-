from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


class Student(models.Model):
    Male = 'male'
    Female = 'female'
    Gender = (
        (Male, 'Male'),
        (Female, 'Female'),
            )

   # is used to store the image file according to user's id with the file name.
    def image_directory(instance, filename):
        print(dir(instance))
        return 'user_{0}/{1}'.format(instance.owner.id, filename)

    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    profile_image = models.ImageField(upload_to=image_directory, blank=True, null=True)
    prefect = models.CharField(max_length=40, blank=True, null=True)
    parent_confirmation = models.BooleanField(verbose_name="parent confirmation status", blank=True, null=True)
    
    def __str__(self):
        return self.student_user.first_name

class Parent (models.Model):
    Single = 'sngl'
    Together = 'tgther'
    Splitted = 'splttd'
    Divorced = 'dvcd'
    Deceased_partner = 'dcsd_ptner'

    Marrital_status = (
        (Single, 'Single'),
        (Together, 'Together'),
        (Splitted, 'Splitted'),
        (Divorced, 'Divorced'),
        (Deceased_partner, 'Deceased_partner'),
            )

    Male = models.CharField(max_length=20, blank=True, null=True)
    Female = models.CharField(max_length=30, blank=True, null=True)
    male_tel_number = models.CharField(max_length=30, blank=True, null=True)
    female_tel_number = models.CharField(max_length=30, blank=True, null=True)
    male_email = models.EmailField(null=True, blank=True)
    female_email = models.EmailField(null=True, blank=True)
    marriage = models.CharField(max_length=15, blank=True, null=True, choices=Marrital_status)
    ward = models.ManyToManyField(Student)
