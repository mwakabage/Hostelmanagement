from django.forms import ModelForm,forms
from .models import Room



# class RoomAssignment(ModelForm):
#     class Meta:
#         model=RoomAssignment 
#         fields=('room_number','capacity','occupants','status')
      
class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields=('room_number','capacity','occupants','status')
        


# class RoomSelection(forms.form):
#     room = forms.ModelChoiceField(
#         queryset=Room.objects.filter(occupants__lt=models.F('capacity')),
#         empty_label="Select a Room",
#         label="Available Rooms"
#     )
#     def save(self,user):
#       room = self.cleaned_data['room']
#       #this checks if user choose the room already
#       if RoomAssignment.objects.filter(user=user).exists():
#         raise forms.ValidationError("You have already choose a room.")
        
#     # Assign room
#       RoomAssignment.objects.create(user=user, room=room)

#     # Update room users
#       room.occupants += 1
#       room.save()