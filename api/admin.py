from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Category, Article


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Article)
# admin.site.register(Message)
# admin.site.register(MessageResponse)

