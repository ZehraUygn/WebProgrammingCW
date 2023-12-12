from django.contrib import admin
from .models import User, Category, NewsArticle, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(NewsArticle)
admin.site.register(Comment)