from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "last_updated"]
    list_filter = ['timestamp', 'last_updated']

    search_fields = ['title', 'content']

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)