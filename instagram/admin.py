from django.contrib import admin

from instagram.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'photo', 'caption', 'location']


@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
