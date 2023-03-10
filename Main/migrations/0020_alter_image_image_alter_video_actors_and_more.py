# Generated by Django 4.1.3 on 2022-12-21 19:37

from django.db import migrations, models

import Main.models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0019_rename_img_bgimage_image_rename_img_mainimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=Main.models.image_name),
        ),
        migrations.AlterField(
            model_name='video',
            name='actors',
            field=models.ManyToManyField(blank=True, null=True, to='Main.actor'),
        ),
        migrations.AlterField(
            model_name='video',
            name='coutries',
            field=models.ManyToManyField(blank=True, null=True, to='Main.country'),
        ),
        migrations.AlterField(
            model_name='video',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='Main.genre'),
        ),
        migrations.AlterField(
            model_name='video',
            name='producers',
            field=models.ManyToManyField(blank=True, null=True, to='Main.producer'),
        ),
    ]
