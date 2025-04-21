from .models import User
from django.forms import ModelForm
from .models import Suggestion,Announcement


class Suggestions(ModelForm):
    class Meta:
        model=Suggestion 
        fields=('suggestion',)
class OfficialNews(ModelForm):
    class Meta:
        model=Announcement
        fields=('user','title','announcement')
  