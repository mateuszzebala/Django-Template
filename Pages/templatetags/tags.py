from django import template
from Pages.models import Language, ToTranslate, Translated, Page
from django.shortcuts import reverse
register = template.Library()


def make_editable(text, string, key, main, config):
    main = -1 if main is None else main.id
    if config['request'].user.groups.filter(name = "Page Editor").exists():
        return f"<editable class='editable' text='{text}' main='{main}' key='{key}'>{string}</editable>"
    else:
        return string

@register.simple_tag
def text(text, config):
    lang = Language.objects.filter(name=config['lang']).first()
    maintext = ToTranslate.objects.filter(text=text).first()
    txt = Translated.objects.filter(maintext=maintext, language=lang).first()
    string = text
    key = -1
    if txt is not None:
        string = txt.content
        key = txt.id
    return make_editable(text, string, key, maintext, config)

@register.simple_tag
def languages():
    return Language.objects.all()


@register.simple_tag(takes_context=True)
def translate(context, text):
    lang = context['page'].language
    print(lang)
    return str(lang)


@register.simple_tag(takes_context=True)
def meta_tags(context):
    return ""

@register.simple_tag(takes_context=True)
def link(context, name):
    lang = context['page'].language.name
    return reverse("Pages:page", kwargs={'page':name, 'lang':lang})


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.simple_tag
def images(path):
    return f"/images/{path}"

@register.simple_tag
def videos(path):
    return f"/videos/{path}"

@register.simple_tag
def audios(path):
    return f"/audios/{path}"
