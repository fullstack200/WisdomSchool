from django.urls import reverse
import boto3
import os
from django.db.models.signals import pre_delete
from django.db.models.signals import post_delete
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


class YearOfExam(models.Model):
    year_of_exam = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.year_of_exam)

class DistinctionHolder(models.Model):
    toppers = models.ForeignKey(YearOfExam, related_name='distinction_holders', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    marks = models.IntegerField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f"{self.name} ({self.toppers.year_of_exam})"


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
            
@receiver(post_delete, sender=YearOfExam)
def remove_file_from_s3_toppers(sender, instance, using, **kwargs):
    # Loop through all related distinction holders
    for distinction in instance.distinction_holders.all():
        if distinction.image:
            # Delete the associated image file
            distinction.image.delete(save=False)
            
@receiver(post_delete, sender=DistinctionHolder)
def remove_file_from_s3_distinction(sender, instance, using, **kwargs):
    # Check if the DistinctionHolder instance has an image and delete it from S3
    if instance.image:
        instance.image.delete(save=False)  # Delete image from the storage

    
