from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("email", "name", "is_staff", "id")
    ordering = ("email",)


admin.site.register(User, UserAdmin)
