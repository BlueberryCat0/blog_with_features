from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q

# Create your views here.
from apps.posts.models import Post
from .documents import PostDocument


class SearchView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        if q:
            posts = PostDocument.search().query("match", title=q)
            # firstFilter = Q("match", title=q)
            # secondFilter = Q("match", text=q)
            # combinedFilter = firstFilter | secondFilter
            # posts = PostDocument.search().query('bool', filter=[combinedFilter])
            posts = posts.to_queryset()
        else:
            posts = ''

        context = {
            'posts':posts,
        }
        print(posts)
        return render(request, 'search/search.html', context)
