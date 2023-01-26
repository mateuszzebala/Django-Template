from django.contrib import admin

from .models import Profile, View


@admin.register(Profile)
class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'datetime']

@admin.register(View)
class VisitAdmin(admin.ModelAdmin):
    list_display = ["id", "datetime", "user", "ip_v4", "url"]
    list_filter = ['datetime', 'user', 'ip_v4', 'url', 'method']