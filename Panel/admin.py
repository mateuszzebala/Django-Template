from django.contrib import admin
from .models import Command, Message

@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ['id', 'command']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['email', 'datetime', 'readed']
    list_filter = ['readed', 'datetime']