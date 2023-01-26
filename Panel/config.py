from django.contrib.auth.models import User, Group
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import UserCreationForm
from Panel.models import Message, Command

registered_models = [
    (Group, ("id", "name")),
    (User, ("id", "username", "email", "first_name", "last_name")),
    (Session, ("session_key",)),
    (Message, ('id', 'email', 'datetime', 'readed')),
    (Command, ('id', 'name', 'command'))
]


registered_pages = []

registered_forms = []

def register_model(model, fields):
    """
    :param model: Model
    :param fields: First should be a primary key
    :return: None
    """
    registered_models.append((model, fields))


def register_page(url, name, icon):
    registered_pages.append({
        "name":name,
        "icon":icon,
        "url":url,
    })


def register_form(name, form, model):
    registered_forms.append({
        "id": len(registered_forms),
        "name": name,
        "form": form,
        "model": model
    })


register_form("New User", UserCreationForm, User)

