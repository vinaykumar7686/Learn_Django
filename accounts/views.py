from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout, get_user_model

from .forms import LoginForm,RegisterForm
from django.shortcuts import redirect

User = get_user_model()

# Create your models here.
def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        email = form.cleaned_data.get('email')

        try:
            user = User.objects.create_user(username = username, password = password, email = email)
        except Exception as e:
            print(e)
            user = None

        if user!=None:
            login(request, user)
            print('Registered')

            return redirect('/')
        else:
            print("Not Registered")
            return render(request, 'login/register.html', {'form':form})
    
    return render(request, 'login/register.html', {'form':form})





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
            print('unable to authenticate')
            pass

    form = LoginForm()
    return render(request, "login/login.html", {"form":form})


def logout_view(request):
    print('Current User: ',request.user)
    if request.user:
        logout(request)
    return redirect("/login/")