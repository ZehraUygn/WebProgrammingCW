from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile,  Product, Message, MessageResponse


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Message)
admin.site.register(MessageResponse)

