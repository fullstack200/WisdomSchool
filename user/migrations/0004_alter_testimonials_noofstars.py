# Generated by Django 4.2.4 on 2023-08-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_testimonials_noofstars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='noOfStars',
            field=models.IntegerField(),
        ),
    ]
