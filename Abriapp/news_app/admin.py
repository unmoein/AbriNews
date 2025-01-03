from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, News, Comment, Like

class UserAdmin(BaseUserAdmin):
    list_display = ('mobile_number', 'role', 'is_staff', 'is_superuser')
    search_fields = ('mobile_number',)
    ordering = ('mobile_number',)
    fieldsets = (
        (None, {'fields': ('mobile_number', 'password')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile_number', 'password1', 'password2', 'role'),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Like)


# Register your models here.
