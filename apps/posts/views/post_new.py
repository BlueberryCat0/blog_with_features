from django.views.generic import View
from ..forms import PostForm
from ..models import Post, PostImage
from django.http import HttpResponse
import json
from django.shortcuts import render, redirect

class PostNewView(View):
    def get(self, request):
        post = Post.objects.create()
        form = PostForm(initial={'post_id': post.id})
        context = {
            'form': form,
        }
        return render (request, 'posts/post_new.html', context)

    def post(self, request):
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post_id = form.cleaned_data['post_id']
            post = Post.objects.get(id=post_id)
            post.title = form.cleaned_data['title']
            post.preview_image = form.cleaned_data['preview_image']
            post.is_created = True
            post.save()
        return redirect('/')


class PostImageView(View):
    def post(self, request):
        file = request.FILES['image']
        post_id = request.POST.get('post_id')
        status = 500
        if file:
            post = Post.objects.get(id=post_id)
            post_image = PostImage.objects.create(
                post=post,
                img=file,
            )
            img_url = post_image.img.url
            status=200
            response_data = {
                'img_path': img_url,
                'img_pk': post_image.pk,
            }

        return HttpResponse(json.dumps(response_data), status=status)


class PostImageDeleteView(View):
    def post(self, request, *args, **kwargs):
        img_pk = request.POST.get('img_pk')
        img = PostImage.objects.get(pk=int(img_pk))
        img.delete()
        status = 200
        data = {
            'status': 'ok'
        }
        return HttpResponse(json.dumps(data), status=status)

























    #
