from django.db import models
from django.utils import timezone
from django.conf import settings
from uuid import uuid4
from Level.models import Level

# Create your models here.


# is used to store the image file according to user's id with the file name.
def photo_upload(instance, filename):
    return "Student/{0} {1}/profile_image/{2}".format(
        instance.first_name, instance.last_name, filename
    )


class Student(models.Model):
    Male = "male"
    Female = "female"
    Gender = (
        (Male, "Male"),
        (Female, "Female"),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name="user account", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=223, null=True, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    other_names = models.CharField(max_length=500, null=True, blank=True)
    uuid = models.CharField(max_length=4000, default=uuid4())
    date_of_birth = models.DateField(
        blank=True, null=True, auto_now_add=False, auto_now=False
    )
    current_location = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    # class_room = models.ForeignKey("Class_Room", on_delete=models.CASCADE)
    # teachers = models.ManyToManyField("Teacher")
    # class_teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    disability = models.CharField(max_length=400, null=True, blank=True)
    illness = models.CharField(max_length=500, null=True, blank=True)
    allergies = models.CharField(max_length=410, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender)
    profile_image = models.ImageField(upload_to=photo_upload, blank=True, null=True)
    religion = models.CharField(max_length=30, null=True, blank=True)
    home_town = models.CharField(max_length=100, null=True, blank=True)
    other_name = models.CharField(max_length=200, null=True, blank=True)
    is_rep = models.BooleanField(default=False)
    is_class_rep = models.BooleanField(default=False)
    parent_confirmation = models.BooleanField(
        verbose_name="parent confirmation status", blank=True, null=True
    )
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)

    current_level = models.CharField(max_length=255, blank=True, null=True)
    Marrital_status = (
        ("Gaurdian", "Gaurdian"),
        ("Single", "Single"),
        ("Together", "Together"),
        ("Married", "Married"),
        ("Splitted", "Splitted"),
        ("Divorced", "Divorced"),
        ("Deceased_partner", "Deceased_partner"),
    )
    biological_parent = models.BooleanField(blank=True, null=True)
    mother_fullname = models.CharField(max_length=255, blank=True, null=True)
    father_fullname = models.CharField(max_length=255, blank=True, null=True)
    mother_date_of_birth = models.DateField(blank=True, null=True, auto_now_add=False)
    father_date_of_birth = models.DateField(blank=True, null=True, auto_now_add=False)
    mother_phone = models.CharField(max_length=255, blank=True, null=True)
    father_phone = models.CharField(max_length=255, blank=True, null=True)
    mother_email = models.CharField(max_length=255, blank=True, null=True)
    father_email = models.CharField(max_length=255, blank=True, null=True)
    parent_marrital_status = models.CharField(
        choices=Marrital_status, blank=True, null=True, max_length=16
    )

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Student profile"
        verbose_name_plural = "Student profiles"


# end of the student profile class......................................................


prefect_type = (
    ("G", "Global"),
    ("C", "ClassRoom"),
    ("O", "Other"),
)


class Prefect(models.Model):
    title = models.CharField(max_length=255)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)
    prefect_type = models.CharField(
        max_length=1, choices=prefect_type, null=True, blank=True
    )

    def __str__(self):
        return self.title
