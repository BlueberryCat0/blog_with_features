from ..models import Post
from django.contrib import admin
from .post_image import PostImageInline

class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostImageInline,
    ]
