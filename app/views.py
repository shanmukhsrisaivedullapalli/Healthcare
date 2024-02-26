from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Medication
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login')
def home(request):
    success_message = messages.get_messages(request)
    if request.method == 'POST':
        medication_name = request.POST.get('medication_name')
        medication_time = request.POST.get('medication_time')
        if medication_name and medication_time:
            medication = Medication(user=request.user, name=medication_name, time=medication_time)
            medication.save()
            messages.success(request, 'Medication added successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid form submission.')
    medications = Medication.objects.filter(user=request.user)
    return render(request, 'home.html', {'medications': medications,'success_message': success_message})

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return redirect('user_login')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created successfully. You can now log in.')
            return redirect('user_login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})