from django.contrib import admin
from .models import Room, RoomAssignment

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display =["room_number","capacity","occupants","status"]

class RoomAssignmentAdmin(admin.ModelAdmin):
    list_display =["document_pdf","room_verification","user"]
    
 
 
admin.site.register(RoomAssignment,RoomAssignmentAdmin)
admin.site.register(Room,RoomAdmin)
 