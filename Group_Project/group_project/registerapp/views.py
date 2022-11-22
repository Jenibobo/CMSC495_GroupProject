from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def registerView(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()   
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)