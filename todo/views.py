from django.shortcuts import render, redirect
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def add_todo(request):
    task = request.POST.get('task')
    Task.objects.create(task=task, complete=False)
    return redirect(to=index)


def do_todo(request, id):
    task = Task.objects.get(id=id)
    task.complete = True
    task.save()
    return redirect(to=index)


def undo_todo(request, id):
    task = Task.objects.get(id=id)
    task.complete = False
    task.save()
    return redirect(to=index)