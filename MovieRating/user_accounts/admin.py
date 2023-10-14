from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import your custom user model
from .forms import UserCreateForm  # Import your custom form

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'age')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

