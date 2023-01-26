from django.contrib.auth.models import User
from django.urls import reverse

from Account.models import Profile
from Panel.utils import render
from Panel.views.panel import is_superuser


class Users:
    @is_superuser
    def main(request):
        users = []
        if request.GET.get('q') is not None:
            users = User.objects.filter(username__contains=request.GET.get('q')).order_by('is_staff').reverse()
        else:
            users = User.objects.all().order_by('is_staff').reverse()

        return render(request, "Panel/Pages/users.html", {
            "path": {
                "USERS": reverse('Panel:users'),
            },
            "users":users,
            "q":request.GET.get('q')
        })

    @is_superuser
    def user(request, id):

        user = User.objects.filter(id=id).first()
        profile = Profile.objects.filter(user=user).first()
        password_edited = False

        if request.method == "POST":
            email = request.POST.get("email")
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            password = request.POST.get("password")
            bio = request.POST.get("bio")
            image = request.FILES.get("image")

            if not None in [username, first_name, last_name]:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.save()

            if email is not None:
                user.email = email
                user.save()

            if image is not None:
                if profile is not None:
                    profile.image = image
                    profile.save()
                else:
                    profile = Profile(image=image, user=user)
                    profile.save()

            if bio is not None:
                if profile is not None:
                    profile.bio = bio
                    profile.save()
                else:
                    Profile(bio=bio, user=user).save()

            if password is not None:
                user.set_password(password)
                user.save()

        user = User.objects.filter(id=id).first()
        return render(request, "Panel/Pages/user.html", {
            "path":{
                "USERS": reverse('Panel:users'),
                user.username: reverse('Panel:users-user', kwargs={"id": id}),
            },
            "user":user,
            "password_edited":password_edited,
            "profile":profile
        })