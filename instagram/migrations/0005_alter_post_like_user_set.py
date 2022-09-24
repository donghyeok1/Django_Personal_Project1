# Generated by Django 4.0.7 on 2022-09-24 12:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0004_post_like_user_set_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='like_post_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
