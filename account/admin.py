from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Profile


class UserAdmin(DefaultUserAdmin):
    model = Profile
    list_display = ('username', 'dashboard_id', 'last_login')
    fieldsets = (
        (None, {
            'fields': ('username', 'dashboard_id', 'password')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'dashboard_id', 'password1', 'password2'),
        }),
    )
admin.site.register(Profile, UserAdmin)
