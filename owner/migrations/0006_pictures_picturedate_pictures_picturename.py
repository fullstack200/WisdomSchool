# Generated by Django 4.2.4 on 2023-09-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0005_rename_topperimage_toppers_topper1image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='pictureDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pictures',
            name='pictureName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
