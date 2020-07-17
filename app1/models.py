from django.db import models

class User_registration(models.Model):
    idno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50,unique=True)
    Phone_Number = models.IntegerField(unique=True)
    Email = models.EmailField(unique=True)