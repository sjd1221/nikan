from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    (None, {'fields': ('Hospital',)}),
)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'Hospital')

admin.site.register(User, CustomUserAdmin)