from django.views.generic import ListView
from ..models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'posts/posts.html'

    def get_queryset(self):
        context = super().get_queryset()
        context = context.filter(is_created=True)
        return context
