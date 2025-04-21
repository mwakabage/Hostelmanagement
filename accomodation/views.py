from django.shortcuts import render,redirect
from django.contrib.auth import checks
from django.contrib import messages
from .models import User,Room
from .forms import RoomForm

# Create your views here.

#let's create another room 
def createRoom(request):
    if request.method=="POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RoomForm()
        
    return render(
        request,'accomodation/create_room.html',{  "form":form,
                                                        "room_number":form["room_number"],
                                                        "capacity":form["capacity"],
                                                        "occupants":form["occupants"],
                                                        "status":form["status"]
                                                        }
        
    )
    
        
#check the available rooms

def select_room(request,pk):
    
    user=User.objects.get(email=request.user)  
    if user.room_number is None or user.room_number =='Not Yet Assigned':
        room=Room.objects.get(id=pk)
        user.room_number=room.room_number
        user.save()
        capacity=room.capacity
        occupants=room.occupants
        room.occupants=occupants+1
        room.capacity=capacity-1
        room.save()
        messages.success(request, f"You have successfully selected Room {room.room_number}!",extra_tags="room selected")
        #return redirect('dashboard') 
        return redirect('dashboard')
    
    messages.warning(request, "You can not hold two rooms at once",extra_tags="room selection failed")   
    return redirect('dashboard')





def release_room(request,pk):
     user=User.objects.get(id=pk)  
     user.room_number='Not Yet Assigned'
     user.save()
     
     return redirect('dashboard')
     
