from django.shortcuts import render
from .utils import get_page
import json
from .models import Language, Translated, ToTranslate, Page
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

_render = render


def render(request, template, args={}, content_type=None, status=None, using=None):
    args['languages'] = Language.objects.all()
    return _render(request, template, args, content_type, status, using)


def httpcode(request, code, message):
    return ...


def page(request, language, page_name):
    current_page = get_page(language, page_name)
    if current_page is None:
        return httpcode(request, 404, "Page not found")
    else:
        return render(request, current_page.file, {
            "page": current_page
        })


def default_index(request):
    pg = page(request, 'pl', 'index')
    return pg


@csrf_exempt
def translate(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        lang = Language.objects.filter(name=json_data['language']).first()
        for i, value in json_data['data'].items():
            html, main, text, key = value['html'], value['main'], value['text'], value['key']
            if str(main) == "-1":
                main = ToTranslate(text=text)
                main.save()
            else:
                main = ToTranslate.objects.filter(id=int(main)).first()
            if key != "-1":
                txt = Translated.objects.filter(text=main, language=lang).first()
                txt.content = html
            else:
                txt = Translated(language=lang, orginal=main, text=html)

            txt.save()
        return JsonResponse({"save": True})
    else:
        return JsonResponse({"save": False})
