from django.http import FileResponse
from Panel.utils import render
from .models import Image


def httpcode(request, code=200, message=""):
    return render(request, "Main/httpcode.html", {"code": code, "message": message})

def error404(request):
    return httpcode(request, 404, "Page does not exits")

def image(request, id):
    image = Image.objects.filter(id=id).first()
    return FileResponse(open(image.image.path, "rb"))

def images(request, path):
    try:
        return FileResponse(open(f"Media/images/{path}", "rb"))
    except:
        return httpcode(request, 404, "Image does not exist")

def videos(request, path):
    try:
        return FileResponse(open(f"Media/videos/{path}", "rb"))
    except:
        return httpcode(request, 404, "Video does not exist")

def audios(request, path):
    try:
        return FileResponse(open(f"Media/audios/{path}", "rb"))
    except:
        return httpcode(request, 404, "Audio does not exist")