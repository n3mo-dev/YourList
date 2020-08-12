from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Todo

def homepage(request):
    return render(request, 'homepage.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:        
        form = UserRegisterForm()
    return render(request, 'register.html', {'form' : form})


@login_required
def profile(request):
    user = request.user 
    item = Todo.objects.filter(user=user)
    
    return render(request, 'profile.html',  { 'item' : item })

def addtodo(request):
    data = request.POST['data']
    item = Todo(Data=data)
    item.save()
    return HttpResponseRedirect('/profile/')

def deletetodo(request, itemid):
    item  = Todo.objects.get(id=itemid)
    item.delete()
    return HttpResponseRedirect('/profile/') 




