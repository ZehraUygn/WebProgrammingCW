# api/urls.py
from django.urls import path
from .views import main_spa, SignUpView, LogInView, LogoutView, get_articles, post_article, update_article, delete_article
from .views import get_comments, post_comment, update_comment, delete_comment

urlpatterns = [
    path('', main_spa, name='index'),
    path('signup/', SignUpView, name='signup'),
    path('login/', LogInView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('articles/', get_articles, name='get_articles'),
    path('articles/post/', post_article, name='post_article'),
    path('articles/update/<int:article_id>/', update_article, name='update_article'),
    path('articles/delete/<int:article_id>/', delete_article, name='delete_article'),
    path('articles/<int:article_id>/comments/', get_comments, name='get_comments'),
    path('articles/<int:article_id>/comments/post/', post_comment, name='post_comment'),
    path('comments/update/<int:comment_id>/', update_comment, name='update_comment'),
    path('comments/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]
