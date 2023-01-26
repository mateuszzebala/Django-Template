from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models

from Panel.config import register_model


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Media/Account/images/', null=True, blank=True)
    bio = models.TextField(default="")
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user}"

class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    method = models.CharField(max_length=10, null=True, blank=True, default=None)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)
    ip_v4 = models.CharField(max_length=20, null=True, blank=True)
    url = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.method}] {self.url}"


register_model(Profile, ("id", "user", "datetime"))
register_model(View, ("id", "datetime", "user", "ip_v4"))

