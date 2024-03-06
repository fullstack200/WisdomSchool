from re import T
from django.db import models

# Create your models here.

class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    emailOrPhone = models.CharField(max_length=50,blank=True)
    comments = models.TextField(max_length=500)

    def __str__(self):
        return self.name[:50]

