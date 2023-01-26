from django.db import models
from Panel.config import register_model

class Language(models.Model):
    name = models.CharField(max_length=3)
    long_name_en = models.CharField(max_length=32, default="")
    long_name = models.CharField(max_length=32)

    def __str__(self):
        return self.long_name_en

class Page(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=128, default="")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.CharField(max_length=32)
    public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class ToTranslate(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.content[0:30]

class Translated(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    orginal = models.ForeignKey(ToTranslate, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.maintext.content[0:30]

register_model(Language, ('id', 'name'))
register_model(ToTranslate, ('id', 'text'))
register_model(Translated, ('id', 'language', 'text'))
