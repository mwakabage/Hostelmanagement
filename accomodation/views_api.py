from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RoomSerializer, RoomAssignmentSerializer
from .models import Room, RoomAssignment

@api_view(['GET', 'POST'])
def room_list_create(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def room_detail(request, pk):
    try:
        room = Room.objects.get(pk=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def room_assignment_list_create(request):
    if request.method == 'GET':
        room_assignments = RoomAssignment.objects.all()
        serializer = RoomAssignmentSerializer(room_assignments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def room_assignment_detail(request, pk):
    try:
        room_assignment = RoomAssignment.objects.get(pk=pk)
    except RoomAssignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomAssignmentSerializer(room_assignment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RoomAssignmentSerializer(room_assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        room_assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)