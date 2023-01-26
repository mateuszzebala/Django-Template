from django.contrib import admin
from .models import Language, Translated, ToTranslate, Page

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(ToTranslate)
class ToTranslateAdmin(admin.ModelAdmin):
    def get_first_letters(self, item):
        if len(item.content) >= 30:
            return item.content[:30] + "..."
        else:
            return item.content

    list_display = ['id', 'get_first_letters']

@admin.register(Translated)
class TranslatedAdmin(admin.ModelAdmin):
    def get_first_letters(self, item):
        if len(item.content) >= 30:
            return item.content[:30] + "..."
        else:
            return item.content
    list_display = ['id', 'get_first_letters', 'language']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'file']
