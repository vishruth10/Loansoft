from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
DEPT = [('CS','CS'),('IS','IS'),('EC','EC'),('Civil','Civil'),('NTD','NTD'),('MECH','MECH'),('MATHS','MATHS'),('PHYSICS','PHYSICS'),('CHEMISTRY','CHEMISTRY'),('LIBRARY','LIBRARY')]
Gender=[('M','M'),('F','F')]
loans=[(100000,100000),(50000,50000),(0,0)]
class Lecturers(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email_id=models.EmailField()
    address=models.TextField(max_length=150)
    aadhar_number=models.CharField(max_length=20)
    pan_card_number=models.CharField(max_length=20)
    department=models.CharField(max_length=20,choices=DEPT)
    gender=models.CharField(max_length=20,choices=Gender)
    shared_amount=models.IntegerField(default=0)
    loan_balance=models.IntegerField(choices=loans)
    loan_left=models.IntegerField(default=0)
    emi=models.IntegerField(default=0)
    savings=models.IntegerField(default=0)
    def __str__(self):
        return str(self.username)
class History(models.Model):
    username=models.ForeignKey(Lecturers,on_delete=models.CASCADE)
    hemi=models.IntegerField()
    loan_left=models.IntegerField(default=0)
    date=models.DateField()
        

# Create your models here.