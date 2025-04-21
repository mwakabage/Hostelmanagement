from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm,ProfileForm
from django.contrib import messages
from .models import User 
from  accomodation.models import Room
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required




# Create your views here.
def login_form(request):
    if request.method == "POST":
       email=request.POST.get("email")
       password=request.POST.get("password") 
       user=authenticate(email=email,password=password)
    
    
       if user is not None:
          login(request,user)
          return redirect("dashboard")
       else:
            messages.error(request, "Invalid username or password",extra_tags="login error")
            
            
    return render(request,"authentication/authenticate.html")
    
def register_form(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        
        if form.is_valid():
            user=form.save(commit=False)
            user.password=make_password(form.cleaned_data["password"])
            user.role="STUDENT"
            user.save()
            messages.success(request,"Registered successfull!!!",extra_tags="registration passed")
            return redirect("login")
       
      
    else:
        form=UserForm()
    return render(request,'authentication/Register.html',{ 
                                                          
                                                        "first_name":form["first_name"],
                                                        "middle_name":form["middle_name"],
                                                        "last_name":form["last_name"],
                                                        "email":form["email"],
                                                        "phone_number":form["phone_number"],
                                                        "password":form["password"],
                                                                        #    "form":form,
                                                                          
                                                                          })
def dashboard(request):
    rooms= Room.objects.filter(status='Not Full')
    users=User.objects.filter(email=request.user)
    return render(request,'accomodation/Dashboard.html',{"users":users})


def logout_view(request):
    logout(request)
    return redirect('login')


def available_rooms(request):
   rooms= Room.objects.filter(status='Not Full')
   return render(request,'accomodation/rooms.html',{'rooms': rooms})

def edit_profile(request):
    
    
    
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user)
        
      
        if form.is_valid():
           form.save()
           return redirect('dashboard')
       
    else:
           form = ProfileForm(instance=request.user)
    return render(request,'accomodation/edit_profile.html',{'form':form})