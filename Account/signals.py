# from django.db.models.signals import pre_delete
# from django.dispatch import receiver
# from .models import Student
# import os
# from django.db import models

# @receiver(models.signals.post_delete, sender=Student)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` object is deleted.
#     """
#     if instance.file:
#         if os.path.isfile(instance.file.path):
#             os.remove(instance.file.path)