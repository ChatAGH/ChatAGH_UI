from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from .forms import RegisterForm


class SignInView(LoginView):
    """Username+password login using our template."""

    template_name = "accounts/login.html"


class SignOutView(LogoutView):
    """Logs out and redirects to login page."""

    def get_next_page(self) -> str:
        return reverse("accounts:login")


def register(request: HttpRequest) -> HttpResponse:
    """
    Handle new user registration.
    On success, logs the user in and redirects to chat index.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("chat:index")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})
