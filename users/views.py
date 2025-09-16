from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AccountCreationForm


class SignUpView(CreateView):
    form_class = AccountCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")  # <- no trailing slash


class LoginView(DjangoLoginView):
    template_name = "login.html"
