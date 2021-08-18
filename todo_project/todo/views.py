from django.shortcuts import render, redirect

from .models import SingleTodo

from .forms import SingleTodoForm


def home_page(request):
    context = {
        'todos': SingleTodo.objects.all()
    }
    return render(request, 'todo/home.html', context)


def add_todo(request):
    if request.method == 'POST':
        form = SingleTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-home')
    else:
        form = SingleTodoForm()
    return render(request, 'todo/add-todo.html', {'form': form})


def update_todo(request, todo_id):
    todo = SingleTodo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect('todo-home')


def delete_todo(request, todo_id):
    SingleTodo.objects.filter(id=todo_id).delete()
    return redirect('todo-home')


def about_page(request):
    return render(request, 'todo/about.html')
