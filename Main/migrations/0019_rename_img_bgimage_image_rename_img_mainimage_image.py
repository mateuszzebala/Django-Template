# Generated by Django 4.1.3 on 2022-12-19 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0018_rename_image_bgimage_img_rename_image_mainimage_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bgimage',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='mainimage',
            old_name='img',
            new_name='image',
        ),
    ]
