from django.db import models

class user(models.Model):
    user_name = models.CharField(max_length=50,null=True,blank=True) 
    email = models.EmailField(max_length=50,null=True,blank=True) 
    password1 = models.CharField(max_length=50,null=True,blank=True)
    password2 = models.CharField(max_length=50,null=True,blank=True)
