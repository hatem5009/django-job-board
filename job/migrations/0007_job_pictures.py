# Generated by Django 3.0.8 on 2020-08-02 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pictures',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
