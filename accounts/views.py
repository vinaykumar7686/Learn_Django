from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm
from django.shortcuts import redirect

# Create your models here.

def login_view(request):

    form = LoginForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(request, username = username, password = password)

        if user:
            # provide access
            login(request, user = user)
            return redirect("/")
        else:
            # redirect somewhere else
            #request.session['Invalid_User'] = 1 
            pass

    form = LoginForm()
    return render(request, "login/login.html", {"form":form})


def logout_view(request):
    print('Current User: ',request.user)
    if request.user:
        logout(request)
    return redirect("/login/")