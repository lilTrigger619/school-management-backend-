from django.db import models
from base_user_manager.models import C_user
from uuid import uuid4


# Create your models here.
def profile_image(instance, filename):
    return 'Staff/user_{0}/{1}'.format(instance.user.username, filename)


Gender = (('mal', 'Male'), ('fem', 'Female'))


#admin to register staff will use this function to upload to the directory
def photo_upload(instance, filename):
    return 'staff/{0} {1}/profile_image/{2}'.format(instance.first_name,
                                                    instance.last_name,
                                                    filename)


class Staff(models.Model):
    user = models.OneToOneField(C_user, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    uuid = models.CharField(max_length=4000, default=uuid4())
    position = models.CharField(max_length=48, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=244, null=True, blank=True)
    disability = models.CharField(max_length=255, null=True, blank=True)
    illness = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(
        max_length=3,
        choices=Gender,
    )
    profile_image = models.ImageField(upload_to=photo_upload,
                                      blank=True,
                                      null=True)

    def __str__(self):
        return self.first_name


'''
class Photo(models.Model):
    uuid = models.ForeignKey(max_length=4000)
    photo = models.ImageField(upload_to=photo_upload)
'''
