from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegistrationForm


class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('index')
    # success_url = 'games'


class UserLogoutView(LogoutView):
    template_name = 'auth/logout.html'

    def get_success_url(self):
        return reverse_lazy('login')


class RegisterView(CreateView):
    template_name = 'auth/register.html'
    form_class = RegistrationForm
    body = '''
    
    '''

    def get_success_url(self):
        return reverse_lazy('index')
