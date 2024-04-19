from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, logout
from .models import CustomUser

# Create your views here.


def check_who_loggedin(request):
    user = request.user
    print(user)
    if user.is_authenticated:
        if user.is_superuser:
            return redirect("products:dashboard")
        else:
            return redirect("products:add_sales")
    else:
        return redirect("authentication:login")


def signup(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            email = form.cleaned_data["email"]
            phone_no = form.cleaned_data["phone_no"]
            full_name = form.cleaned_data["full_name"]
            print(username, email, password2, password1, phone_no, full_name)
            if password1 != password2:
                print("password not match")
                return redirect("signup")
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password1,
                phone_no=phone_no,
                full_name=full_name,
            )
            user.save()
            return redirect("authentication:login")
        else:
            print("invaild input")
    else:
        form = forms.SignupForm()
        print("not post")
    context = {"form": form}
    return render(request, "authentication/signup.html", context)


def logout_user(request):
    logout(request)
    return redirect("authentication:login")
