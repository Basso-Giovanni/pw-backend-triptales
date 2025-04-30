from django.urls import path
from posts.views import TopLikedPostsView, UserTopLikesView, UserTopPostsView
from .views import CreateTripGroupView, JoinTripGroupView, TripGroupPostsListView

urlpatterns = [
    path('create/', CreateTripGroupView.as_view(), name='create-trip'),
    path('join/<int:pk>/', JoinTripGroupView.as_view(), name='join-trip'),
    path('<int:group_id>/posts/', TripGroupPostsListView.as_view(), name='group-posts'),
    path('<int:group_id>/top-like/', TopLikedPostsView.as_view(), name='group-top-liked-posts'),
    path('<int:group_id>/top-like-user/', UserTopLikesView.as_view(), name='group-top-liked-users'),
    path('<int:group_id>/top-posters/', UserTopPostsView.as_view(), name='group-top-posters'),
]
