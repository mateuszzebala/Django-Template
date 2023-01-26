
from Panel.views.panel import render
from django.shortcuts import redirect
from django.conf import settings
from Panel.views.panel import httpcode

import os

ext = {
    "img": ('jfif', 'jpg', 'gif', 'png', 'bmp', 'webp', 'tiff', 'psd', 'raw', 'heif'),
    "vid": ('avi', 'mov', 'mp4', 'wmv', 'flv', 'm4v', 'webm', '3gp', 'mkv', 'ogv'),
    "aud": ('aif', 'aiff', 'au', 'mid', 'midi', 'mp3', 'wav', 'flac', 'ogg', 'wma')
}

def have_ext(name, type):
    if type == 'all':
        tab = ext['img'] + ext['vid'] + ext['aud']
    else:
        tab = ext[type]
    for e in tab:
        if name.endswith(f".{e}"):
            return True

    return False

class Media:
    def main(request):
        return redirect('Panel:media-images')

    def show_image(request):
        path = "" if request.GET.get('path') is None else request.GET.get('path')
        path = path.split('/')
        for i in path:
            if i == "":
                path.remove(i)
        if len(path) < 1:
            return httpcode(request, 404, "Image doesn't exists")

        return render(request, "Panel/Pages/media/show-image.html", {
            "img": {"name": path[-1], "path": "/".join(path), "parent":"/".join(path[:-1])}
        })
    def images(request):
        path = "" if request.GET.get('path') is None else request.GET.get('path')
        path = path.split('/')
        for i in path:
            if i == "":
                path.remove(i)
        print(path)
        folders = []
        list_dir = os.listdir(f'{settings.BASE_DIR}/Media/images/{"/".join(path)}')
        for elem in list_dir:

            if not os.path.isdir(f'Media/images/{"/".join(path)}/{elem}'):
                if not have_ext(elem, "img"):
                    list_dir.remove(elem)
            else:
                folders.append({
                    "name": elem,
                    "path": f"{'/'.join(path)}/{elem}"
                })
                list_dir.remove(elem)


        return render(request, "Panel/Pages/media/images.html", {
            "images": list_dir,
            "folders": folders,
            "up": "/".join(path[:-1])
        })

    def videos(request):
        list_dir = os.listdir('Media/videos')
        for elem in list_dir:
            if not os.path.isdir(f'Media/videos/{elem}'):
                if not have_ext(elem, "vid"):
                    list_dir.remove(elem)

        return render(request, "Panel/Pages/media/videos.html", {
            "videos": list_dir
        })

    def audios(request):
        list_dir = os.listdir('Media/audios')
        for elem in list_dir:
            if not os.path.isdir(f'Media/audios/{elem}'):
                if not have_ext(elem, "aud"):
                    list_dir.remove(elem)

        return render(request, "Panel/Pages/media/audios.html", {
            "audios": list_dir
        })

    def copy(request, type):
        red = None
        if type == "image":
            red = redirect('Panel:media-show-image')
        red['Location'] += f"?path={request.GET.get('path')}"
        return red

    def cut(request, type):
        red = None
        if type == "image":
            red = redirect('Panel:media-show-image')
        red['Location'] += f"?path={request.GET.get('path')}"
        return red