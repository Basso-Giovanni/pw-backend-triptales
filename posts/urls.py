from django.urls import path
from comments.views import CommentListCreateView, CommentDetailView
from .views import CreatePostView, PostDetailView, like_post, unlike_post

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/like/', like_post, name='like-post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike-post'),
    path('<int:post_pk>/comments/', CommentListCreateView.as_view(), name='post-comments'),
    path('<int:post_pk>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
