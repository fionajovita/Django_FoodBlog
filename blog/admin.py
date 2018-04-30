from django.contrib import admin
from .models import Post,Tag


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","created_date","published_date "]
    list_display_links = ["created_date"]
    list_filter = ["created_date","published_date"]
    class Meta:
        model = Post

admin.site.register(Post)

admin.site.register(Tag)