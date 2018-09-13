from django.views.generic import ListView
from ..models import Post
from ..forms import SearchForm


class PostListView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'posts/posts.html'

    def get_context_data(self):
        context = super(PostListView, self).get_context_data()
        context['search_form'] = SearchForm()
        return context

    def get_queryset(self):
        context = super().get_queryset()
        context = context.filter(is_created=True)
        return context
