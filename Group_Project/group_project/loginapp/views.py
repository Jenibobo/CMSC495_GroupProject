
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


# Create your views here.

def loginView(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

# def logout_view(request):
#     logout(request)
#     messages.info(request, "Logged out successfully")

