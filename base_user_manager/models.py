from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    BaseUserManager,
    AbstractBaseUser,
)
from django.utils import timezone

# Create your models here.


# This is to manage the custom student user model
class CustomUserManager(BaseUserManager):
    # student user with no privilages.
    def create_basic(self, username, email, password, **other_fields):
        if bool(username):
            email = self.normalize_email(email)
            basic_profile = self.model(username=username, email=email, **other_fields)
            basic_profile.set_password(password)
            basic_profile.is_active = True
            basic_profile.is_admin = False
            basic_profile.is_superuser = False
            basic_profile.is_sys_admin = False
            basic_profile.is_student = False
            basic_profile.is_staff = False
            basic_profile.save()
            return basic_profile
        else:
            raise ValueError("A valid username is required!")

    # end of create_basic method .............................

    # create_student_user
    def create_student_user(self, username, email, password, **other_fields):
        student = self.create_basic(
            username=username, email=email, password=password, **other_fields
        )
        student.is_active = True
        student.is_student = True
        student.save()
        return student

    # end of create_student_user method .............................

    # staff user with only staff privilages.
    def create_staff_user(self, username, email, password=None, **other_fields):

        staff = self.create_basic(
            username=username, email=email, password=password, **other_fields
        )
        staff.is_active = True
        staff.is_staff = True
        staff.save()
        return staff

    # end of create_staff_user method.............................

    # admin user with staff and admin privilages.
    def create_admin_user(self, username, email, password=None, **other_fields):
        admin = self.create_basic(
            username=username, password=password, email=email, **other_fields
        )
        admin.is_active = True
        admin.is_admin = True
        admin.save()
        return admin

    # superuser with all privilages.
    def create_superuser(self, username, email, password=None, **other_fields):
        superuser = self.create_basic(
            username=username, email=email, password=password, **other_fields
        )
        superuser.is_active = True
        superuser.is_admin = True
        superuser.is_superuser = True
        superuser.has_perm("base_user_manager.Modify or add data")
        superuser.save()
        return superuser


# custom user model {C_user}
class C_user(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # date_joined = models.DateTimeField(default=timezone.now())
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_sys_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 

    objects = CustomUserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        permissions = [
            ("Modify or add data", "The user can create or add students"),
        ]

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)
