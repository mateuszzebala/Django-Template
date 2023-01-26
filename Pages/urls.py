from django.urls import path
from . import views

app_name = 'Pages'

urlpatterns = [
    path('translate/', views.translate, name="translate"),
    path('<language>/<page_name>/', views.page, name='page'),
    path('', views.default_index, name="default_index"),
]