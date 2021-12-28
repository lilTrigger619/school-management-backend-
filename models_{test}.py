from django.db import models

# Create your models here.

class FileTest(models.Model):
    def File_Dire(instance, filename):
        dir(instance)
        return 'user_{0)/{1}'.format(instance.id, filename)

    image = models.ImageField(upload_to = File_Dire)
    
