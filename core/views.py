from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import MyUser as User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):

    return render(request, 'core/index.html', {
        'categories': [],
        'items': [],
    })

def contact(request):
    return render(request, 'core/contact.html')

def log_in(request):
    if request.user.username != "":
        return redirect('/')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else: 
            form = LoginForm
            return render(request, 'authentication/login.html', {
                'form': form,
                'error_message': 'Email or password is incorrect'
            })
    
    else: 
        form = LoginForm

    return render(request, 'authentication/login.html', {
        'form': form
    })


def signup(request):
    if request.method == 'POST':
        new_user = request.POST
        form = SignupForm(new_user)

        if User.objects.filter(username=new_user['username']).exists() or User.objects.filter(email=new_user['email']).exists():
            # User already exists, handle accordingly (e.g., display an error message)
            return render(request, 'authentication/signup.html', {'form': form, 'error_message': 'User already exists'})
        else:
            if form.is_valid():
                form.save()

                return redirect('/login/')
        

    else:
        form = SignupForm()

    return render(request, 'authentication/signup.html', {
        'form': form
    })


def forgot_password(request):
    return render(request, 'authentication/forgot-password.html')

