# Generated by Django 4.1.4 on 2022-12-26 13:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Account', '0003_remove_visit_session_remove_visit_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccountImage',
            new_name='ProfileImage',
        ),
    ]