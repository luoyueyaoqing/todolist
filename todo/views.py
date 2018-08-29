from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from .models import Todo, User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def index_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not User.objects.filter(username=username).exists():
            if password1 == password2:
                User.objects.create_user(username=username, password=password1)
                messages.success(request, '注册成功')
                return redirect(to='login')
            else:
                messages.warning(request, '两次密码输入不一致')
        else:
            messages.warning(request, "账号已存在")
    return render(request, 'register.html')


def index_login(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if next_url:
                return redirect(next_url)
            return redirect('index')
        return HttpResponseRedirect(request.get_full_path())
    return render(request, 'login.html', {'next_url': next_url})


@login_required
def index(request):
    users = User.objects.all()
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'index.html', {'todos': todos, 'users': users})


def user_page(request):
    uid = request.GET.get('uid')
    todo_user = get_object_or_404(User, id=uid)
    todos = Todo.objects.filter(user=todo_user)
    return render(request, 'user_page.html', locals())


@login_required
def add_todo(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method != "POST":
        messages.warning(request, "请求方法不对")
    else:
        task = request.POST.get('task')
        if task:
            if Todo.objects.filter(task=task).exists():
                messages.warning(request, '任务已存在')
            else:
                Todo.objects.create(user=user, task=task, complete=False)
                messages.success(request, '任务添加成功')
        else:
            messages.warning(request, '请输入任务')
    return redirect(to=index)


@login_required
def do_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if todo:
        todo.complete = True
        todo.save()
        messages.success(request, '任务已完成')
    else:
        messages.warning(request, '操作失败')
    return redirect(to=index)


@login_required
def del_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if todo:
        todo.delete()
        messages.success(request, '任务已删除')
    else:
        messages.warning(request, '操作失败')
    return redirect(to=index)
