import platform
import sys

from django.conf import settings as djangoSettings
from django.contrib.auth import login as login_user, authenticate
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import FileResponse
from django.shortcuts import redirect

from Panel.config import registered_models
from Panel.utils import *
from Panel.utils import render


def is_superuser(fnc):
    def inner(*args, **kwargs):
        request = args[0]
        if request.user.is_superuser:
            return fnc(*args, **kwargs)
        else:
            return redirect("Panel:login")

    return inner

@is_superuser
def httpcode(request, code=200, message=""):
    if not request.user.is_superuser: return redirect("Panel:login")
    return render(request, "Panel/Pages/httpcode.html", {"code":code, "message":message}, status=int(code))

@is_superuser
def error404(request):
    return httpcode(request, 404, "Page does not exists")

@is_superuser
def home(request):


    return render(request, "Panel/Pages/home.html", {
        "machine": platform.machine(),
        "system": platform.system(),
        "server_name": platform.uname().node,
        "python": sys.version.split(" ")[0],
        "debug":djangoSettings.DEBUG,
        "time_zone":djangoSettings.TIME_ZONE,
        "installed_apps":len(djangoSettings.INSTALLED_APPS),
        "db_type":djangoSettings.DATABASES['default']['ENGINE'].split('.')[-1],
        "today_views":len(View.objects.filter(datetime__lt=datetime.datetime.now()-datetime.timedelta(days=1))),
        "number_of_users":len(User.objects.all())
    })



@is_superuser
def settings(request):
    if request.method == "POST":
        content = request.POST.get("content").encode()
        with open("Django" + os.sep + "settings.py", "wb") as file:
            file.write(content)
    with open("Django" + os.sep + "settings.py", "r") as file:
        return render(request, "Panel/Pages/settings.html", {
            "content": "".join(file.readlines())
        })



def get_app_models():
    mdls = {}
    for model, fields in registered_models:
        if mdls.get(model._meta.app_label) is None:
            mdls[model._meta.app_label] = []
        mdls[model._meta.app_label].append(model.__name__)
        
    return mdls

def get_model_names():
    names = []
    for model, fields in registered_models:
        names.append(model.__name__)
    return names



def login(request):
    if request.user.groups.filter(name="Panel user").exists():
        return redirect('Panel:home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username is not None and password is not None:
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request, 'Panel/login.html', {"bad_data":True})
            else:
                login_user(request, user)
                if user.groups.filter(name="Panel user").exists():
                    return redirect('Panel:home')
                else:
                    return redirect('Main:default_index')



    return render(request, 'Panel/login.html', {})

@is_superuser
def logout_user(request, id):
    user = User.objects.filter(id=id).first()
    if user is not None:
        sessions = Session.objects.all()
        for session in sessions:
            if int(session.get_decoded().get('_auth_user_id')) == user.id:
                session.delete()

    return redirect("Panel:users-user", id=id)


@is_superuser
def local_file(request):
    if request.GET.get("p") is not None:
        try:
            return FileResponse(open(request.GET.get("p"), "rb"))
            res = redirect("Panel:editor-file")
            res['Location'] += f"?p={request.GET.get('p')}"
            return res
        except FileNotFoundError:
            return httpcode(request, 404, "File does not exist")
    else:
        return httpcode(request, 404, "File does not exist")
