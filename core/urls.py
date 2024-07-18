from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.log_in, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('reset-password/<str:uidb64>/<str:token>/', views.reset_password, name='reset-password'),
    path('complete-register/<str:token>/', views.complete_register, name='complete-register')
]