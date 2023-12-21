"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.main_spa),
    path('signup/', views.signupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logout, name='logout'),
    path('api/profile/', views.profile, name='profile'),
    path('api/profile/<int:profile_id>', views.profile_api, name="api-profile"),
    path('api/articles/', views.articles_api, name="api-articles"),
    path("api/articles/<int:article_id>", views.article_api, name="api-article"),
    path("api/comment/", views.comments_api, name="api-comment"),

]
