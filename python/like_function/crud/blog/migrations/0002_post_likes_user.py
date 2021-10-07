# Generated by Django 3.2 on 2021-09-28 11:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_user',
            field=models.ManyToManyField(blank=True, related_name='like_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
