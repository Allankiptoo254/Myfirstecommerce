from django.db import models


# Create your models here.
class Signup(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=50,choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M')


    def __str__(self):
        return self.first_name + '' + self.last_name