# Generated by Django 4.1.3 on 2022-11-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_alter_page_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='html_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
