# Generated by Django 4.2.4 on 2023-08-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_toppers'),
    ]

    operations = [
        migrations.AddField(
            model_name='toppers',
            name='topperMarks',
            field=models.IntegerField(default=90),
            preserve_default=False,
        ),
    ]
