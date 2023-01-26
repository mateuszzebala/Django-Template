
from django.urls import path
from Panel.config import register_page
from . import views

app_name = 'Account'

urlpatterns = [
    path('image/<id>', views.image, name="image"),
    path('csrf/', views.csrf, name="csrf"),
    path('me/', views.me, name="me"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('views/', views.view, name="views"),
]

register_page('Account:views', "Views", '<i class="fa-regular fa-eye"></i>')