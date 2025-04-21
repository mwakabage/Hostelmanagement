from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
# from .models import students,block_leader,block_warden
from django.contrib.auth.admin import UserAdmin

class UserAdminModel(UserAdmin):
    ordering=['id']
    search_fields=['last_name',]
    list_display=[
        'email','first_name','last_name','password','phone_number','room_number','profile_image','bio','is_active','is_staff','is_superuser','role'
    ]
    fieldsets=(
       
        (
        None,
        {
          'fields':('email','first_name','last_name','room_number','profile_image','bio','is_active','is_staff','is_superuser','role')
        },
        ),
    )
    add_fieldsets = (
        ( 
         None, 
         {
           "classes":('wide',),
           "fields": (
               "email","password1","password2",
               "first_name","last_name","room_number",'profile_image','bio',"is_active","is_staff","is_superuser",'role'
           ),
       },
         ),
   )
   
# Register your models here.
admin.site.register(User,UserAdminModel)