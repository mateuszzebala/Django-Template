import datetime

from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.models import User
from django.http import FileResponse
from django.http import JsonResponse
from django.middleware.csrf import get_token
from Panel.views.panel import render as panel_render

from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from Panel.views.panel import is_superuser
from Panel.utils import render
from .models import Profile, View
from django.db.models import Count


def httpcode(request, code=200, message=""):
    return JsonResponse({
        "code": code,
        "message": message
    }, status=code)


def image(request, id):
    user = User.objects.filter(id=id).first()
    profile = Profile.objects.filter(user=user).first()
    file = ""
    image = False
    if profile is not None:
        image = profile.image

    print(image)
    if not image:
        file = "Media/account/images/default.png"
    else:
        file = profile.image.path
    if user is not None:
        return FileResponse(open(file, 'rb'))


@csrf_exempt
def csrf(request):
    return JsonResponse({
        "token": get_token(request)
    })


def account(request):
    return render(request, "Account.html", {})


def me(request):
    if request.user.is_authenticated:
        return JsonResponse({
            "login": True,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "username": request.user.username,
            "email": request.user.email,
            "image": reverse("Account:image", kwargs={"id": request.user.id}),
            "superuser": request.user.is_superuser,
            "date_joined": request.user.date_joined,
            "staff": request.user.is_staff,
            "active": request.user.is_active,
            "last_login": request.user.last_login,
            "datetime": datetime.datetime.now()
        })
    else:
        return httpcode(request, 200, "You are not logged in")


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login_user(request, user)
        return httpcode(request, 200, "Login successful")
    else:
        return httpcode(request, 200, "Bad data")


def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User(username=username, password=password)
    user.save()
    return httpcode(request, 200, "User created")


@is_superuser
def view(request):
    asc = request.GET.get('asc') == "on"
    count = request.GET.get('count') == "on"
    try:
        datefrom = datetime.datetime.strptime(request.GET.get('from'), "%Y-%m-%dT%H:%M")
    except:
        datefrom = None

    try:
        dateto = datetime.datetime.strptime(request.GET.get('to'), "%Y-%m-%dT%H:%M")
    except:
        dateto = None

    order_by = request.GET.get('order-by') if request.GET.get('order-by') is not None else 'dcount'

    views = None
    query = {}
    if datefrom is not None and dateto is not None:
        query = {"datetime__gte": datefrom, "datetime__lte": dateto}
    elif datefrom is not None:
        query = {"datetime__gte": datefrom}
    elif dateto is not None:
        query = {"datetime__lte": dateto}

    if count:
        views = View.objects.filter(**query).values('url').annotate(count=Count('url'))
    else:
        views = View.objects.filter(**query)

    if not asc:
        views = views.reverse()

    return panel_render(request, "views.html", {
        "views": views,
        "count": count,
        "asc": asc,
        "datefrom": None if datefrom is None else datefrom.strftime("%Y-%m-%dT%H:%M"),
        "dateto": None if dateto is None else dateto.strftime("%Y-%m-%dT%H:%M"),
        "order_by": order_by
    })
