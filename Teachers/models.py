from django.db import models
from base_user_manager.models import C_user

# Create your models here.
def profile_image(instance, filename):
    return '{0}/profile_image/{1}'.format(instance.user.username, filename)
        
Gender = (('mal', 'Male'), ('fem', 'Female'))

class Staff(models.Model):
    user = models.OneToOneField(C_user, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=profile_image, blank=True, null=True)
    position = models.CharField(max_length=48, blank=True, null=True) 
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=244, null=True, blank=True)
    #classes = models.ManyToManyField('ClassRoom') called in ClassRooms.models.
    disability = models.CharField(max_length=255, null=True, blank=True)
    illness = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=3, choices = Gender,)

    def __str__(self):
        return self.user.first_name
