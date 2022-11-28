from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CreateUserForm


def registerView(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()   
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'register.html', context)