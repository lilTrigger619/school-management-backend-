from django.db import models
from django.contrib.auth.models import  PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.utils import timezone

# Create your models here.

# This is to manage the custom student user model
class CustomUserManager(BaseUserManager):
    #student user with no privilages.
    def create_student_user(self, username, email, password=None, **other_fields):
        if not username:
            raise ValueError('A proper username is required')
        else:
            email = self.normalize_email(email)
            student = self.model(username=username, email=email)
            student.set_password(password)
            student.is_active=True
            student.is_student=True
            student.save()
            return student
    #staff user with only staff privilages.
    def create_staff_user(self, username, email, password=None, **other_fields):
        if not username:
            raise ValueError('A proper username is required')
        else:
            email = self.normalize_email(email)
            staff = self.model(username=username, email=email)
            staff.set_password(password)
            staff.is_active = True
            staff.is_staff = True
            staff.save()
            return staff
    #admin user with staff and admin privilages.
    def create_admin_user(self, username, email, password=None, **other_fields):
        if not username:
            raise ValueError("A proper username is required")
        else:
            email = self.normalize_email(email)
            admin = self.model(username=username, email=email)
            admin.set_password(password)
            admin.is_active = True
            admin.is_staff = True
            admin.is_admin = True
            admin.save()
            return admin
    #superuser with all privilages.
    def create_superuser(self, username, email, password=None, **other_fields):
        superuser = self.create_admin_user(username=username, email=email, password=password)
        superuser.is_active=True
        superuser.is_student=True
        superuser.is_staff=True
        superuser.is_admin=True
        superuser.is_superuser=True
        superuser.has_perm('base_user_manager.Modify or add data')
        superuser.save()
        return superuser


#custom user model {C_user}
class C_user(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(blank=True, )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now())
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        permissions = [
        ('Modify or add data', 'The user can create or add students'),
                ]
    
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
