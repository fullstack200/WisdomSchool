from re import T
from django.db import models

# Create your models here.

class Enquiries(models.Model):
    name = models.CharField(max_length=50,null = True)
    studentPhone = models.CharField(max_length=50,null = True)
    studentEmail = models.CharField(max_length=50,null = True)
    message = models.TextField(max_length=500,null = True)

    def __str__(self):
        return self.name[:50]
