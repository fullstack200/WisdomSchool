from django.urls import reverse
import boto3
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db import models
# Create your models here.

class Pictures(models.Model):
    pictureType = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True,upload_to='media/')
    pictureName = models.CharField(max_length=50,null=True,blank=True)
    pictureDate = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.pictureName

class Toppers(models.Model):
    yearOfexam = models.IntegerField()
    topper1Name = models.CharField(max_length=50)
    topper1Marks = models.IntegerField()
    topper1Image= models.ImageField(upload_to='media/')
    topper2Name = models.CharField(max_length=50)
    topper2Marks = models.IntegerField()
    topper2Image= models.ImageField(upload_to='media/')
    topper3Name = models.CharField(max_length=50)
    topper3Marks = models.IntegerField()
    topper3Image= models.ImageField(upload_to='media/')

 def __str__(self):
        return str(self.yearOfexam)


class Announcements(models.Model):
    announcementName = models.CharField(max_length=50)
    announcement = models.CharField(max_length=200)

    def __str__(self):
        return self.announcementName
    
@receiver(models.signals.post_delete, sender=Pictures)
def remove_file_from_s3_pic(sender, instance, using, **kwargs):
    image_fields = ['picture']
    for field_name in image_fields:
        # Get the image field value
        image_field = getattr(instance, field_name)
        if image_field:
            # Delete the image file
            image_field.delete(save=False)
            
@receiver(models.signals.post_delete, sender=Toppers)
def remove_file_from_s3_toppers(sender, instance, using, **kwargs):
    image_fields = ['topper1Image','topper2Image','topper3Image']
    for field_name in image_fields:
        # Get the image field value
        image_field = getattr(instance, field_name)
        if image_field:
            # Delete the image file
            image_field.delete(save=False)

    
