from django.urls import path

from .import views

urlpatterns = [
     path('annoucement/',views.listOfAnnouncemnt,name="annoucement"),
     path('suggestion/',views.studentSuggestion,name='suggestion'),
]