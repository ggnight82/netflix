"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username','rating','pk', 'date_joined', 'last_login', 'is_admin', 'is_superuser',)
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User)