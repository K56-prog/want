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
            return render(request, 'signup.html', {'some':100})
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

class WantList(ListView):
    template_name = 'list.html'
    model = WantModel

class WantUpdate(UpdateView):
    template_name = 'update.html'
    model = WantModel
    fields = {'title', 'field', 'memo'}
    success_url = reverse_lazy('list')

class WantDetail(DetailView):
    template_name = 'detail.html'
    model = WantModel

class WantCreate(CreateView):
    template_name = 'create.html'
    model = WantModel
    fields = {'title', 'field', 'memo'}
    success_url = reverse_lazy('list')

class WantDelete(DeleteView):
    template_name = 'delete.html'
    model = WantModel
    success_url = reverse_lazy('list')

def resultfunc(request):
    try:
        pk = random.randint(1, WantModel.objects.count())
        object = WantModel.objects.get(pk=pk)
        return render(request, 'result.html', {'object':object})
    except:
        return render(request, 'random.html', {'error':'もう一回「ガシャる」ボタンを押してください。'})

def randomfunc(request):
    return render(request, 'random.html', {})

