from django.urls import path
from .views import AddPostView, PostView, GetPostsView

urlpatterns = [
    path('posts/', AddPostView().as_view(), name = 'add-post'),
    path('posts/<int:post_id>/', PostView().as_view(), name = 'post-details'),
    path('posts/list/', GetPostsView().as_view(), name = 'all-posts'),


]
