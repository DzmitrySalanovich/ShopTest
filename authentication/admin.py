from django.contrib import admin
from authentication.models import User, UserManager


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass