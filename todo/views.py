from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TaskForm
from .models import Todo

# Create your views here.
def view_todos(request):
    tasks = Todo.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, 'tasks': tasks}
    return render(request, 'todo/index.html', context)

def update_todo(request, id):
    tasks = Todo.objects.get(id=id)

    form = TaskForm(instance=tasks)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'todo/update.html', context)


def delete_todo(request, id):
    item = Todo.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        messages.success(request, item.task + " has been removed.")
        return redirect('index')

    context = {'item': item}
    return render(request, 'todo/delete.html', context)

def complete_task(request, id):
    tasks = Todo.objects.get(id=id)
    tasks.completed = True
    tasks.save()
    messages.success(request, tasks.task + " has been completed.")
    return redirect('index')