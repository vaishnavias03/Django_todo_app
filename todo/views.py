from .forms import TodoForm
from .models import Todo
from django.http.response import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    todoform = TodoForm()
    context ={'form': todoform}
    return render(request, 'add.html', context)

def todolist(request):
    todoList = Todo.objects.order_by('id')
    context = {'todoList': todoList}
    return render(request, 'todolist.html', context)

def add(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        newtodo = Todo(title = request.POST['title'], desc = request.POST['desc'])
        newtodo.save()
    return redirect('todolist')

def deletetodo(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.delete()
    return redirect('todolist')

def edittodo(request, todo_id):
    todo = Todo.objects.get(pk= todo_id)
    todo.delete()
    form = TodoForm( instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            
            return redirect('todolist')
    
    context = {'form': form}
    return render(request, 'edittodo.html', context)

def complete(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.complete = True
    todo.save()

    return redirect('todolist')
