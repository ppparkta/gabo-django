from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST) #POST로 받아온 값으로 form의 데이터를 채울 것을 의미함
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form': form})

def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo) #POST로 받아온 데이터로 form을 채울 것이고, 대상(instance)은 todo
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form': form})

def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html', {'dones': dones})


def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo:todo_list')


