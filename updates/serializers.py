from rest_framework import serializers
from .models import Announcement,Suggestion

class AnnoucementSerializers(serializers.ModelSerializer):
    class Meta:
        model=Announcement
        fields=['title','announcement']
        
class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Suggestion
        fields=['suggestion']
        
        
        
