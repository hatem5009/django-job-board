# Generated by Django 3.0.8 on 2020-08-02 17:49

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='pictures',
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]
