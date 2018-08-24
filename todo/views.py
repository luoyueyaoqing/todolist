from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def add_todo(request):
    if request.method != "POST":
        messages.warning(request, "请求方法不对")
    else:
        task = request.POST.get('task')
        if task:
            if Task.objects.filter(task=task).exists():
                messages.warning(request, '任务已存在')
            else:
                Task.objects.create(task=task, complete=False)
                messages.success(request, '任务添加成功')
        else:
            messages.warning(request, '请输入任务')
    return redirect(to=index)


def do_todo(request, id):
    task = get_object_or_404(Task, id=id)
    if task:
        task.complete = True
        task.save()
        messages.success(request, '任务已完成')
    else:
        messages.warning(request, '操作失败')
    return redirect(to=index)


def del_todo(request, id):
    task = get_object_or_404(Task, id=id)
    if task:
        task.delete()
        messages.success(request, '任务已删除')
    else:
        messages.warning(request, '操作失败')
    return redirect(to=index)