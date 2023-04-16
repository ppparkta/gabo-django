from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo

# Create your views here.
# 전체 투두 조회
def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todoApp/todo_list.html', {'todos': todos})

# 투두 상세정보 조회 (제목, 설명)
def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todoApp/todo_detail.html', context={'todo': todo})

# 투두 생성
def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todoApp:todo_list')

    else:
        form = TodoForm()

    return render(request, 'todoApp/todo_post.html', context={'form': form})

# 투두 수정
def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todoApp:todo_list')

    else:
        form = TodoForm(instance=todo)

    return render(request, 'todoApp/todo_post.html', context={'form': form})

# 완료된 투두 조회
def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todoApp/done_list.html', context={'dones': dones})

# 투두 완료시키기
def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todoApp:todo_list')