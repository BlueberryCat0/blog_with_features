from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(
        blank=True,
        max_length=100,
        verbose_name="Заголовок"
        )
    text = models.TextField(
        blank=True,
        max_length=512,
        verbose_name='Текст'
    )
    preview_image = models.ImageField(
        upload_to="posts/preview_images/%Y/%m/%d",
        verbose_name="Превью изображение"
        )
    is_created = models.BooleanField(
        default=False,
        verbose_name='Создан'
    )
    created_at = models.DateTimeField(
        default=datetime.now,
        blank=True,
        verbose_name='Дата создания'
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"
