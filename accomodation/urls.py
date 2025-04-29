from django.urls import path

from .import views,views_api

urlpatterns = [
     path('room_selection/<int:pk>/',views.select_room, name="select_room"),
     path('create_room/',views.createRoom, name="create_room"),
     path('release_room/<int:pk>/',views.release_room, name="release_room"),
     
     
     
     
    #API Part 
    path('api/rooms/', views_api.room_list_create, name='api_room_list'),
    path('api/rooms/<int:pk>/', views_api.room_detail, name='api_room_detail'),
    path('api/room_assignments/', views_api.room_assignment_list_create, name='api_room_assignment_list'),
    path('api/room_assignments/<int:pk>/', views_api.room_assignment_detail, name='api_room_assignment_detail'),

]