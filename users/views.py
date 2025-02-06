from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from traitlets import Instance
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm, UserRwgistrationForm


# Create your views here.


def login(request):
    if request.method == "POST":

        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))

    else:
        form = UserLoginForm()
    context = {"title": "Home - login", "form": form}
    return render(request, "users/login.html", context)



@login_required
def logout(request):
    auth.logout(request)

    context = {"title": "Home - logout"}
    return redirect(reverse("main:index"))


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main:index"))

    else:
        form = UserRegistrationForm()
    context = {"title": "Home - registration", "form": form}
    return render(request, "users/registration.html", context)

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, Instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return ProfileForm(reverse("user:profile"))

    else:
        form = ProfileForm(Instance=request.user)
    context = {
        'title':"Home-Profile",
        'forms':form
    }
    return render(request, "users/profile.html", context)
