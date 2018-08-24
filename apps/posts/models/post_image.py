from django.db import models
from .post import Post

class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="Пост"
    )
    img = models.ImageField(
        upload_to="posts/post_images/%Y/%m/%d",
        verbose_name="Изображение"
    )

    class Meta:
        verbose_name="Картинка из поста"
        verbose_name_plural="Картинки постов"
