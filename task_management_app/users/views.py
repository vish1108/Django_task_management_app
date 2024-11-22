from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .forms import TaskForm


def home(request):
    return render(request, 'home.html')

def logout_views(request):
    logout(request)
    return redirect("/")

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
        
        return render(request, 'task_form.html', {'form': form})
    
    else:
        form = TaskForm()
        return render(request, 'task_form.html', {'form': form})


def task_update(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'task_confirm_delete.html', {'task': task})


