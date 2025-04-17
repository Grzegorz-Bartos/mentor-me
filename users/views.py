from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AccountCreationForm


class SignUpView(CreateView):
    form_class = AccountCreationForm
    success_url = reverse_lazy("login/")
    template_name = "signup.html"


class LoginView(AuthLoginView):
    template_name = "login.html"
