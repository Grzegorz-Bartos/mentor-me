from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class LoginView(AuthLoginView):
    template_name = "login.html"
