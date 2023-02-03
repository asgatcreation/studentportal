from django.shortcuts import redirect, render
from . forms import *
from django.contrib import messages
from django.views import generic


# Create your views here.
# 19:58

def home(request):
    return render(request, "dashboard/home.html")
def notes(request): 
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request, f"Notes Added from {request.user.username} Successfully!")
    else:  
        form = NotesForm()
    notes = Notes.objects.filter(user = request.user)
    context = {
        'notes' : notes,
        'form' : form
    }
    return render(request, "dashboard/notes.html", context)

#delete notes view
def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("dashboard:notes")


#detail view for note

class NotesDetailView(generic.DetailView):
    model = Notes
    #template_name = "TEMPLATE_NAME"

####HOME WORK

def homework(request):
    homework=Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    context = {
        'homeworks':homework,
        'homeworks_done':homework_done
    }
    return render(request, 'dashboard/homework.html', context)
