from django.contrib import admin
from .models import Announcement,Suggestion

# Register your models here.

class AnnouncementAdmin(admin.ModelAdmin):
    list_display =['user','announcement','time','title']
    
    
class SuggestionAdmin(admin.ModelAdmin):
    list_display =['suggestion','time']


admin.site.register(Announcement,AnnouncementAdmin)
admin.site.register(Suggestion,SuggestionAdmin)
