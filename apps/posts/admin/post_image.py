from django.contrib import admin
from ..models import PostImage

class PostImageAdmin(admin.ModelAdmin):
    pass


class PostImageInline(admin.TabularInline):
    model = PostImage
