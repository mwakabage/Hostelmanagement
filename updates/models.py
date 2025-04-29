from django.db import models
from authentication.models import User

# Create your models here.

class Suggestion(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    suggestion=models.TextField(max_length=250,blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True)

class Announcement(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    title=models.CharField(max_length=300,blank=False,null=False)
    time=models.DateTimeField(auto_now_add=True)
    announcement=models.TextField(max_length=250,blank=True,null=True)
    