# Generated by Django 4.2.4 on 2023-08-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_testimonials_noofstars'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='noOfStars',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]