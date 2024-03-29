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
    path('delete_homework/<int:pk>', views.delete_homework, name="delhomework"),
    
    
    path('youtube', views.youtube, name="youtube"),
    
    
    path('todo', views.todo, name="todo"),
    path('update_todo/<int:pk>', views.update_todo, name="updatetodo"),
    path('delete_todo/<int:pk>', views.delete_todo, name="deltodo"),
    
    
    
    path('books', views.books, name="books"),
    
    path('dictionary', views.dictionary, name="dictionary"),
    
    path('wikipedia', views.wikipedia, name="wikipedia"),
    
    path('conversion', views.conversion, name="conversion"),
    
]
