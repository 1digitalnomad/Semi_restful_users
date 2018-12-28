from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request):
    context = {
        'users' : User.objects.all()
    }
    return render(request, 'users/index.html', context)

def new(request):
    return render(request, 'users/usersnew.html')

def edit(request, id):
    context ={
        'user' : User.objects.get(id=id)
    }
    return render(request, 'users/usersedit.html', context)


def create(request):
    User.objects.create_user(request.POST)
    print(request.POST)
    # User.objects.create_user(request.POST)
    return redirect('users:index')

def destroy(request, id):
    User.objects.delete_user(id)
    return redirect('users:index')

def update(request, id):
    User.objects.update_user(request.POST, id)
    return redirect('users:index')

def show(request, id):
    context = {
        'user' : User.objects.get(id=id)
    }
    return render(request, 'users/usersshow.html', context)