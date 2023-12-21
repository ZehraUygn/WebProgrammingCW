from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http.multipartparser import MultiPartParser
from .models import User, Profile
from .forms import SignupForm, LoginForm
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.http import QueryDict
from django.views.decorators.http import require_http_methods


def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

@csrf_exempt
def signupPage(request: HttpRequest) -> HttpResponse:
    """
    Signup function
    Users creating an account
    """

    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # create a new user
            new_user = User.objects.create(username=username, email=email)
            # set user's password
            new_user.set_password(password)
            new_user.save()

            # when a user register, a profile for that user needs to be created
            # a profile must have an email, a DoB and a photograph
            # the photograph and DoB needs to be added by the user - email is set
            new_profile = Profile.objects.create(email=email)
            new_profile.user_acc = new_user
            new_profile.save()

            # authenticate user
            # establishes a session, will add user object as attribute
            # on request objects, for all subsequent requests until logout
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # to be forwarded to the main page - front-end - maybe profile
                return redirect("http://localhost:5173/")

    return render(request, "api/spa/signup.html", {"form": SignupForm})


@csrf_exempt
def loginPage(request: HttpRequest) -> HttpResponse:
    """
    Login function
    Users logging into the app
    """

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # authenticate user to the backend
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("http://localhost:5173/")

                # forward to main page of the application - front-endop")

            # failed authentication
            return render(
                request, "error.html", {"error": "User not registered. Sign up first."}
            )

        # invalid form
        return render(request, "api/spa/login.html", {"form": form})

    return render(request, "api/spa/login.html", {"form": form})


def logout(request: HttpRequest) -> HttpResponse:
    """
    View that can be used for a user to logout
    If the user is authenticated -> They can logout
    """
    if not request.user.is_authenticated:
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))
    else:
        auth.logout(request)
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))
