from django.db import models
from django.utils.text import slugify
from FaceR.models import Org
from django.dispatch import receiver
import os
from django.db.models.signals import post_save

def user_upload_path(instance, filename):
    # Get the user's ID or username
    username = instance.org.name
    filename, extension = os.path.splitext(filename)
    new_filename = f"{instance.enrollment}{extension}"
    return os.path.join(f'{username}/{new_filename}')
    # return f'{username}/{filename}'
class Student(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    enrollment =models.CharField(max_length=50)
    slug = models.SlugField(unique =True , null = True ,blank = True)
    branch = models.CharField(max_length=10)
    adm_year = models.IntegerField()
    image = models.ImageField(upload_to=user_upload_path)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.enrollment)
        return super(Student ,self).save(*args , **kwargs)
    

    def __str__(self): 
        return str(f"Org = {self.org} , enrollment = {self.enrollment} ,branch = {self.branch}")
      
@receiver(models.signals.post_delete, sender=Student)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


class HOD(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=10)
    slug = models.SlugField(unique =True , null = True ,blank = True)
    password = models.CharField(max_length=100)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        return super(HOD ,self).save(*args , **kwargs)

    def __str__(self): 
        return str(f"Org = {self.org} , Branch = {self.branch}")

class TempBranch(models.Model):
    branch =  models.CharField(max_length=10,default="CS")