from django.urls import path
from .views import PostNewView, PostImageView, PostImageDeleteView, PostListView


app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('create/', PostNewView.as_view(), name='post_create'),
    path('add-post-img/', PostImageView.as_view(), name='add_post_img'),
    path('delete-post-img/', PostImageDeleteView.as_view(), name='delete_post_image'),
]
