from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.



class HomepageSlider(models.Model):
    image = models.ImageField(upload_to='media' ,null=True, blank=True)
    
    def __str__(self):
        return self.image
    

    
class HomepageSection1(models.Model):
    course_name = models.CharField(max_length=200, null=True, blank=True)
    course_detail = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return self.course_name
    

    
class HomepageSection2(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    

    
class Blog(models.Model):
    Title = models.CharField(max_length=200, null=True, blank=True)
    Content = RichTextField(null=True, blank=True)
    Imageblog = models.ImageField(upload_to='media')
    Slug = models.SlugField(max_length=200, null=True, blank=True)
    Date_time = models.DateTimeField(null=True, blank=True)
    Keywords = models.CharField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.Title
