from django.db import models
from django.utils.text import slugify

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)
# Create your models here.

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id, extension)


class Job(models.Model): # table in the database

    title = models.CharField(max_length=100) # colonne
    #location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=0)
    pictures = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(blank=True, null=True)

    #codifier le url dans le browser
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args,**kwargs)

    #changer le titre de la page
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
