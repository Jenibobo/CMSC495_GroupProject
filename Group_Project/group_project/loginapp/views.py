from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


# Create your views here.

def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'Welcome {username}!')
        form = AuthenticationForm(data=request.POST)
        return redirect('todo')
    else:
        messages.info(request,f'Account does not exist')
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)
    