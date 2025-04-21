from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.core.exceptions import ValidationError

# Create your models here.
class userManager(BaseUserManager):
    def create_user(self,email,password,**kwargs):
        if not email:
            raise ValueError("please enter correct password/email")
        email=self.normalize_email(email)
        user=self.model(email=email,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
#let's create a super user as a system administrator
    def create_superuser(self,email,password,**kwargs):
       kwargs.setdefault('is_superuser',True)
       kwargs.setdefault('is_staff',True)
       kwargs.setdefault('is_active',True)
       
       user=self.create_user(email,password,**kwargs) 
 
class User(AbstractBaseUser,PermissionsMixin):
    class UserRole(models.TextChoices):
        ADMIN="ADMIN","Admin"
        STUDENT="STUDENT","Student"
        WARDEN="WARDEN","Warden"
        BLOCK_LEADER="BLOCK_LEADER","Block_leader"     
    first_name=models.CharField(max_length=250, blank=True,null=True)
    middle_name=models.CharField(max_length=250,blank=True,null=True)
    last_name=models.CharField(max_length=250,blank=True,null=True)
    email=models.EmailField(max_length=250,null=False,unique=True)
    role=models.CharField(max_length=250,choices=UserRole.choices)
    password=models.CharField(max_length=250,blank=False,null=False)
    phone_number=models.CharField(max_length=20,blank=True,null=True)
    has_room = models.BooleanField(default=False)
    room_number=models.CharField(max_length=250,default='Not Yet Assigned',null=True,blank=True)
    REQUIRED_FIELDS=[]
    USERNAME_FIELD='email'
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False) 
    is_superuser=models.BooleanField(default=False)
    bio=models.TextField(blank=True,null=True)
    profile_image=models.ImageField(upload_to='profile_pics/',default='default.jpg',blank=True,null=True)
    objects=userManager()
   # room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True, blank=True)  # Each student can only belong to one room

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    profile_image=models.ImageField(upload_to='profile_pics/',default='default.jpg')
    
    def __str__(self):
        return f"{self.user.username} Profile"
    