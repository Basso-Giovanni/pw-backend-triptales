from django.urls import path
from posts.views import TopLikedPostsView, UserTopLikesView, UserTopPostsView
from .views import CreateTripGroupView, JoinTripGroupView, TripGroupPostsListView, TripGroupDetailView, \
    MemberBadgeView

urlpatterns = [
    path('create/', CreateTripGroupView.as_view(), name='create-trip'),
    path('info/<group_id>/', TripGroupDetailView.as_view(), name='group-details'),
    path('join/<int:pk>/', JoinTripGroupView.as_view(), name='join-trip'),
    path('<int:group_id>/posts/', TripGroupPostsListView.as_view(), name='group-posts'),
    path('<int:group_id>/top-like/', TopLikedPostsView.as_view(), name='group-top-liked-posts'),
    path('<int:group_id>/top-like-user/', UserTopLikesView.as_view(), name='group-top-liked-users'),
    path('<int:group_id>/top-posters/', UserTopPostsView.as_view(), name='group-top-posters'),
    path('<int:group_id>/badge/<int:user_id>/', MemberBadgeView.as_view(), name='user-group-badge'),
]
