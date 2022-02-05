from django.db import models
from Students.models import Student

# Create your models here.
class Tiution_Fee(models.Model):
    paid = models.DecimalField(decimal_places=2, max_digits=999,default=0)
    amount = models.DecimalField(decimal_places=2, max_digits=999, null=True, blank=True)

class Library_Fee(models.Model):
    paid = models.DecimalField(decimal_places=2, max_digits=999)
    amount = models.DecimalField(decimal_places=2, max_digits=999)

class SRC_Dues(models.Model):
    paid = models.DecimalField(decimal_places=2, max_digits=999)
    amount = models.DecimalField(decimal_places=2, max_digits=999)

class Fees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.CharField(max_length=22)
    level = models.CharField(max_length=22)
    src_dues = models.OneToOneField(SRC_Dues, on_delete=models.CASCADE)
    tiution_fee = models.OneToOneField(Tiution_Fee, on_delete=models.CASCADE)
    library_fee = models.OneToOneField(Library_Fee, on_delete=models.CASCADE)
