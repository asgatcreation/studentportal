from django.urls import path
from . import views 

app_name = 'dashboard'
urlpatterns = [
    path("",views.home, name="home"),
    path('notes', views.notes, name="notes"),
    path('delete_note/<int:pk>', views.delete_note, name="delnote"),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name="notesdetail"),
    
    path('homework', views.homework, name="homework"),
    path('update_homework/<int:pk>', views.update_homework , name="updatehomework"),
    
]
