from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Image


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
