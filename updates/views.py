from django.shortcuts import render,redirect
from .models import Suggestion,Announcement
from .forms import Suggestions




def studentSuggestion(request):
    if request.method == 'POST':
        form = Suggestions(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suggestion')  # Replace 'suggestion' with your success URL name
        else:
            return render(request, 'update/suggestion.html', {"suggestion": form["suggestion"]}) # Pass just the suggestion field.
    else:
        form = Suggestions()
        suggestions=Suggestion.objects.all()

    return render(request, 'update/suggestion.html', {"suggestions":suggestions,"suggestion": form["suggestion"]}) # Pass just the suggestion field.
                                                       
def officialAnnouncemnt(request):
    if request.method =='POST':
        announcement=Announcement(user=request.user,announcement=request.POST.get('suggestion'),
                                  title=request.POST.get('title'))
        announcement.save()
        return redirect()
    return render(request,)

#if user want to see all the announcement announced before
def listOfAnnouncemnt(request):
     announcements=Announcement.objects.all()
     
     return render(request,'update/announcement.html',{"announcements":announcements})

#def listOfSuggestions(request):
 #   suggestions=Suggestion.objects.all()
  #  return render(request,'update/suggestion.html',{"suggestions":suggestions})
