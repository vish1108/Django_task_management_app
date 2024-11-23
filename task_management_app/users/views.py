from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .forms import TaskForm
from django.http import Http404
from .models import UserInvitation



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


def register(request, token):
    try:
        invitation = UserInvitation.objects.get(token=token, is_used=False)
    except UserInvitation.DoesNotExist:
        raise Http404("Invalid or expired invitation.")

    if request.method == 'POST':
        invitation.is_used = True
        invitation.save()

        return redirect('login')

    return render(request, 'register.html', {'invitation': invitation})

def register_without_token(request):
    return render(request, 'users/register.html')



