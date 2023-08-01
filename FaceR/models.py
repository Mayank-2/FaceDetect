from django.contrib.auth.models import User
from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from datetime import timedelta
from django.core.validators import RegexValidator
from datetime import date
# from Account.models import Student


sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
   
# time_slots = (
#     ('7:30 - 8:30', '7:30 - 8:30'),
#     ('8:30 - 9:30', '8:30 - 9:30'),
#     ('9:30 - 10:30', '9:30 - 10:30'),
#     ('11:00 - 11:50', '11:00 - 11:50'),
#     ('11:50 - 12:40', '11:50 - 12:40'),
#     ('12:40 - 1:30', '12:40 - 1:30'),
#     ('2:30 - 3:30', '2:30 - 3:30'),
#     ('3:30 - 4:30', '3:30 - 4:30'),
#     ('4:30 - 5:30', '4:30 - 5:30'),
# )

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)


class Org(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postalcode = models.IntegerField(default=000000)
    email = models.EmailField()

    def __str__(self):
        return str(f"{self.user}_{self.name}")

class AttendanceCS(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    Date = models.DateField(default=date.today)
    name = models.CharField(max_length=30,default="name")
    attendance_date = models.DateTimeField(auto_now_add=True)
    enrollment =models.CharField(max_length=50)
    branch = models.CharField(max_length=10,default="CS")
    adm_year = models.IntegerField(default=2020)

    def __str__(self):
        return str(f"Org = {self.org} , {self.enrollment} , Date = {self.Date}")
    
class AttendanceME(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    Date = models.DateField(default=date.today)
    name = models.CharField(max_length=30,default="name") 
    attendance_date = models.DateTimeField(auto_now_add=True)
    enrollment =models.CharField(max_length=50) 
    branch = models.CharField(max_length=10,default="CS")
    adm_year = models.IntegerField(default=2020)
    
    def __str__(self):
        return str(f"Org = {self.org} , {self.enrollment} , Date = {self.Date}")

class AttendanceCE(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    Date = models.DateField(default=date.today)
    name = models.CharField(max_length=30,default="name")
    attendance_date = models.DateTimeField(auto_now_add=True)
    enrollment =models.CharField(max_length=50)
    branch = models.CharField(max_length=10,default="CS")
    adm_year = models.IntegerField(default=2020)
    
    

    def __str__(self):
        return str(f"Org = {self.org} , {self.enrollment} , Date = {self.Date}")

class AttendanceEC(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    Date = models.DateField(default=date.today)
    name = models.CharField(max_length=30,default="name")
    attendance_date = models.DateTimeField(auto_now_add=True)
    enrollment =models.CharField(max_length=50)
    branch = models.CharField(max_length=10,default="CS")
    adm_year = models.IntegerField(default=2020)
     
    
    def __str__(self):
        return str(f"Org = {self.org} , {self.enrollment} , Date = {self.Date}")
