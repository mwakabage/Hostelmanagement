from django.urls import path

from .import views,views_api

urlpatterns = [
     path('annoucement/',views.listOfAnnouncemnt,name="annoucement"),
     path('suggestion/',views.studentSuggestion,name='suggestion'),
     
     #API Part
    path('announcements/', views_api.announcement_list_create, name='announcement_list_create'),
    path('announcements/<int:pk>/', views_api.announcement_detail, name='announcement_detail'),
    path('suggestions/', views_api.suggestion_list_create, name='suggestion_list_create'),
    path('suggestions/<int:pk>/', views_api.suggestion_detail, name='suggestion_detail'),

]