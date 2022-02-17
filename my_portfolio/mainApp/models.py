from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class TechStack(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MyProject(models.Model):
    title=models.CharField(max_length=255)
    objectives=models.CharField(max_length=300)
    summary=RichTextUploadingField()
    my_role=models.CharField(max_length=200)
    requirement=models.ManyToManyField(TechStack)
    image_thumbnail=models.ImageField(upload_to='project_file')
    source_code=models.URLField(max_length=300)
    demo=models.URLField(max_length=300, blank=True, null=True)


    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


