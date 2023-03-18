from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from users.forms import CustomUserCreationForm


def loginUser(request):
    if request.method == 'POST':

        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usera net')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back :)')
            return redirect('/')
        else:
            messages.error(request, 'username or password are incorrect')
    return render(request, 'users/login.html')

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.username = user_form.username.lower()
            user_form.save()

            messages.success(request, 'User has been created successfully')

            login(request, user_form)
            return redirect('/')
        else:
            messages.error(request, 'SOme Error')

    context = {'form': form}
    return render(request, 'users/register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('/')
