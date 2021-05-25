from django.urls import  path
from . import views 

urlpatterns = [
    path('home/', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('todolist/', views.todolist, name="todolist"),
    path('deletetodo/<todo_id>', views.deletetodo, name="deletetodo"),
    path('edittodo/<todo_id>', views.edittodo, name="edittodo"),
    path('complete/<todo_id>', views.complete, name="complete")
]
