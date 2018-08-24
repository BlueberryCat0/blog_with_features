from django.contrib import admin

from ..models import Post, PostImage

from .post import PostAdmin
from .post_image import PostImageAdmin

admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
