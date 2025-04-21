from django.db import models
from authentication.models import User
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator, MaxValueValidator
formValidator_Ext=FileExtensionValidator(['PDF'])
# Create your models here.
class Room(models.Model):
    ROOM_STATUS_CHOICES = [
        ('Full', 'Full'),
        ('Not Full', 'Not full'),
    ]
 #   user=models.ForeignKey(User,on_delete=models.CASCADE)
    room_number=models.CharField(max_length=25,unique=True)
    capacity=models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(4)])
    occupants=models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(4)])
    status=models.CharField(max_length=10, choices=ROOM_STATUS_CHOICES) 
    def is_full(self):
            return self.occupants >= self.capacity

    def increment_occupants(self):
        if not self.is_full():
            self.occupants += 1
            self.save()  
            return True
        return False

    def __str__(self):
        return f"Room {self.room_number} - {'Full' if self.is_full() else 'Available'}"

class RoomAssignment(models.Model):
    document_pdf=models.FileField(upload_to='documents/',validators=[formValidator_Ext])
    room_verification=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.OneToOneField(Room, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.user.username} -> Room {self.room.room_number}"
    
