# Generated by Django 3.0.8 on 2020-08-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_auto_20200802_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]