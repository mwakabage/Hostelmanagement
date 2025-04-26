from rest_framework import serializers
from .models import Room,RoomAssignment
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'
        


class RoomAssignmentSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    class Meta:
        model=RoomAssignment
        fields=['room_verification','document_pdf','room']
        
        
   
