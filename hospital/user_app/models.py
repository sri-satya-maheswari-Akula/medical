from django.db import models

# Create your models here.



# class Appointment(models.Model):
#     Gender = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('Other', 'Other'),
#     ]
#     Doctors = [

#     ]
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     mobile = models.BigIntegerField()
#     age = models.IntegerField()
#     gender = models.CharField(Gender,default='Male')




class Patient_register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=100)


class Doc_register(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_email = models.EmailField(unique=True)
    doc_mobile = models.BigIntegerField()
    doc_password = models.CharField(max_length=100)

