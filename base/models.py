from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(null=True,blank=True,max_length=150)
    email = models.EmailField(unique=True)
    