from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, CustomPasswordChangeForm, CustomPasswordSendEmailForm
from .models import MyUser as User
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from .utils import send_html_email_with_file, create_link_with_token, is_token_valid
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
import os
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
    form = CustomPasswordSendEmailForm()
    try: 


        if request.method == "POST": 
            owner_email = request.POST['email']
            user = User.objects.get(email=owner_email)


            # Create link
            password_reset_link = create_link_with_token(user)

            to = [owner_email,]
            html_file_path = os.getcwd() + '\\core\\templates\\email_template\\reset-password.html'
            context = {
                'recipient': owner_email, 
                'password_reset_link': password_reset_link,
                'flatform_name': "Mutyses",
                'flatfrom_number_phone': '0972495038',
                'flatform_logo': ''
            }
            subject = 'Password Reset'

            send_html_email_with_file(subject, to, html_file_path, context)

            return render(request, 'authentication/send-email-result.html', context={"sended": True})
    except Exception as e:
        print(e)
        return render(request, 'authentication/send-email-result.html', context={"sended": False})



    return render(request, 'authentication/forgot-password.html', {
        'form': form
    })

def reset_password(request, uidb64, token):
    user_id = urlsafe_base64_decode(uidb64).decode()
    user = User.objects.get(pk=user_id)
    checked_expired: bool = is_token_valid(token, user, 300)


    if checked_expired:

        if request.method == 'POST':
            form = CustomPasswordChangeForm(user, request.POST)
            # Remain error when alway not is_valid => 
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('/')
            else:
                messages.error(request, 'Please correct the error below.')

        else:
            form = CustomPasswordChangeForm(user)


        return render(request, 'authentication/reset-password.html', {'expired': checked_expired, 'form': form})
    else:
        return render(request, 'authentication/reset-password.html', {'expired': checked_expired})

