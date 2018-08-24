from django.db import models

class Post(models.Model):
    title = models.CharField(
        blank=True,
        max_length=100,
        verbose_name="Заголовок"
        )
    preview_image = models.ImageField(
        upload_to="posts/preview_images/%Y/%m/%d",
        verbose_name="Превью изображение"
        )
    is_created = models.BooleanField(
        default=False,
        verbose_name='Создан'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"
