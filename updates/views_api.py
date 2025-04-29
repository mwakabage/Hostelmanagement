from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnnoucementSerializers, SuggestionSerializer
from .models import Announcement, Suggestion



@api_view(['GET', 'POST'])
@csrf_exempt
def announcement_list_create(request):
    if request.method == 'GET':
        announcements = Announcement.objects.all()
        serializer = AnnoucementSerializers(announcements, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AnnoucementSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def announcement_detail(request, pk):
    try:
        announcement = Announcement.objects.get(pk=pk)
    except Announcement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnnoucementSerializers(announcement)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AnnoucementSerializers(announcement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@csrf_exempt
def suggestion_list_create(request):
    if request.method == 'GET':
        suggestions = Suggestion.objects.all()
        serializer = SuggestionSerializer(suggestions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuggestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def suggestion_detail(request, pk):
    try:
        suggestion = Suggestion.objects.get(pk=pk)
    except Suggestion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SuggestionSerializer(suggestion)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuggestionSerializer(suggestion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        suggestion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)