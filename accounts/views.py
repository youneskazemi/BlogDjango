from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm,UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'ورود موفقیت آمیز بود!', 'success')
                return redirect('blog:all_articles')
            else:
                messages.warning(request, 'یوزر یا پسسورد اشتباه است!', 'warning')

    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'با موفقیت خارج شدید!', 'info')
    return redirect("accounts:user_login")


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=email)
            messages.success(request, 'ثبت نام موفقیت آمیز بود!', 'success')
            return redirect('accounts:user_login')

    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})
