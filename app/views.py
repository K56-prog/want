from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import WantModel
from django.urls import reverse_lazy
import random



# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password =request.POST['password']
        try:
            user = User.objects.create_user(username, "", password)
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています。'})
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
            # Redirect to a success page.
            ...
        else:
            return render(request, 'login.html', {})
            # Return an 'invalid login' error message.
            ...
    return render(request, 'login.html', {})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def listfunc(request):
    object_list = WantModel.objects.all()
    user_objects = [v for v in object_list if v.username == request.user.get_username()]
    return render(request, 'list.html',{'user_objects':user_objects})

class WantUpdate(UpdateView):
    template_name = 'update.html'
    model = WantModel
    fields = {'title', 'field', 'memo', 'username'}
    success_url = reverse_lazy('list')

class WantDetail(DetailView):
    template_name = 'detail.html'
    model = WantModel

class WantCreate(CreateView):
    template_name = 'create.html'
    model = WantModel
    fields = {'title', 'field', 'memo', 'username'}
    success_url = reverse_lazy('list')

class WantDelete(DeleteView):
    template_name = 'delete.html'
    model = WantModel
    success_url = reverse_lazy('list')

def resultfunc(request):
    user_objects = [v for v in WantModel.objects.all() if v.username == request.user.get_username()]

    try:
        object_num = random.randint(1, len(user_objects))
        object = user_objects[object_num - 1]
        return render(request, 'result.html', {'object':object})
    except:
        return render(request, 'random.html', {'error':'もう一回「ガシャる」ボタンを押してください。'})

def randomfunc(request):
    return render(request, 'random.html', {})

