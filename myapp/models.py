from django.db import models

# Create your models here.

class Student(models.Model):
    StuId = models.IntegerField()
    StuName = models.CharField(max_length=30)
    Stumarks = models.IntegerField()
    StuEmail = models.EmailField(max_length=20, null=True, blank=True)
    StuImg = models.ImageField(upload_to='images/',null=True, blank=True)