from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http.multipartparser import MultiPartParser
from .models import User, Profile, Category, Article, Comment
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

#SIGNUP
@csrf_exempt
def signupPage(request: HttpRequest) -> HttpResponse:
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(password)
            new_user.save()

            new_profile = Profile.objects.create(email=email)
            new_profile.user_acc = new_user
            new_profile.save()

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                # to be forwarded to the main page - front-end - maybe profile
                return redirect("http://localhost:8000/login")

    return render(request, "api/spa/signup.html", {"form": SignupForm})

#LOGIN
@csrf_exempt
def loginPage(request: HttpRequest) -> HttpResponse:
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("http://localhost:5173")
            return render(
                request, "error.html", {"error": "User not registered. Sign up first."}
            )
        return render(request, "api/spa/login.html", {"form": form})
    return render(request, "api/spa/login.html", {"form": form})

#LOGOUT
def logout(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))
    else:
        auth.logout(request)
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))

#PROFILE
@csrf_exempt
@require_http_methods(['GET'])
def profile(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        if request.method == "GET":
            profile = get_object_or_404(Profile, email=user.email)
            return JsonResponse(
                {
                    "logged_in": True,
                    "username": user.username,
                    "profile": profile.to_dict(),
                }
            )
    else:
        return JsonResponse({"logged_in": False})

#PROFILE API
@csrf_exempt
@require_http_methods(['PUT'])
def profile_api(request: HttpRequest, profile_id: int) -> HttpResponse:
    profile = get_object_or_404(Profile, id=profile_id)
    user = profile.user_acc

    if request.method == 'PUT':
        if request.content_type.startswith('multipart'):
            put, files = request.parse_file_upload(request.META, request)
            request.FILES.update(files)
            request.PUT = put.dict()
        else:
            request.PUT = QueryDict(request.body).dict()

        profile.email = request.PUT["email"]
        user.email = request.PUT["email"]
        user.username = request.PUT["username"]
        profile.date_of_birth = request.PUT["date_of_birth"]
        
        if len(request.FILES.keys())!=0:
            img_data = request.FILES['profile_picture']
            if img_data is not None:
                profile.profile_picture=img_data

        user.save()
        profile.save()
        
        return JsonResponse(
            {
                "logged_in": True,
                "username": user.username,
                "profile": profile.to_dict(),
            }
        )

#ARTICLES API
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def articles_api(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return JsonResponse(
            {
                "articles": [
                    article.to_dict()
                    for article in Article.objects.all()
                ]
            }
        )

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category = request.POST.get("category")
        user = User.objects.get(pk=request.user.id)
        article = Article.objects.create(
            title=title,
            content=content,
            owner=user,
            category=category,
        )
        article.save()
  
        return JsonResponse(
            {
                "articles": [
                    article.to_dict()
                    for article in Article.objects.all()
                ]
            }
        )

#ARTICLE API
@csrf_exempt
@require_http_methods(['PUT'])
def article_api(request: HttpRequest, article_id) -> HttpResponse:
    if request.method == "PUT":
        article = get_object_or_404(Article, id=article_id)
        data = MultiPartParser(request.META, request, request.upload_handlers).parse()[
            0
        ]
        article.save()

        return JsonResponse(
            {
                "articles": [
                    article.to_dict()
                    for article in Article.objects.all()
                ]
            }
        )

# COMMENTS
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def comments_api(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        article_id = request.GET.get("articleId")
        if article_id:
            comments = Comment.objects.filter(article__id=article_id)
        else:
            comments = Comment.objects.all()

        return JsonResponse(
            {
                "comments": [comment.to_dict() for comment in Comment.objects.all]
            }
        )

    user = request.user
    if request.method == "POST" and user.is_authenticated:
        article_id = request.POST.get("articleId")
        text = request.POST.get("text")

        if text and article_id:
            article = Article.objects.get(id=article_id)
            comment = Comment.objects.create(
                article=article,
                text=text,
                user=user,
               
            )
            comment.save()

        return JsonResponse(
            {
                "comments": [commentE.to_dict() for commentE in Comment.objects.all()]
            }
        )
