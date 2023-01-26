from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from django.urls import path, re_path, include
from Main.views import error404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel/', include("Panel.urls")),
    path('Account/', include("Account.urls")),
    path('', include("Main.urls")),
    path('', include("Pages.urls")),
    re_path(r'^static/(?P<path>.*)$', serve, {"document_root": settings.STATIC_ROOT}),
    re_path(r'\w+', error404)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


