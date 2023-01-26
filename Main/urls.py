
from django.urls import path, re_path
from Panel.config import register_page
from . import views
from django.shortcuts import redirect

app_name = 'Main'

def redirect_to_admin(request):
    return redirect('admin:index')

def redirect_to_panel(request):
    return redirect('Panel:home')

urlpatterns = [
    path('admin', redirect_to_admin),
    path('panel', redirect_to_panel),
    re_path(r'^images/(?P<path>.*)$', views.images, name="images"),
    re_path(r'^videos/(?P<path>.*)$', views.videos, name="videos"),
    re_path(r'^audios/(?P<path>.*)$', views.audios, name="audios"),
    path('image/<id>', views.image, name="image"),

]
