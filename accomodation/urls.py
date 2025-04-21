from django.urls import path

from .import views

urlpatterns = [
     path('room_selection/<int:pk>/',views.select_room, name="select_room"),
     path('create_room/',views.createRoom, name="create_room"),
     path('release_room/<int:pk>/',views.release_room, name="release_room"),
]