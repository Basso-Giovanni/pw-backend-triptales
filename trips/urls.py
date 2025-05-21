from django.urls import path
from posts.views import TopLikedPostsView, UserTopLikesView, UserTopPostsView
from .views import CreateTripGroupView, JoinTripGroupView, TripGroupPostsListView, TripGroupDetailView, \
    MemberBadgeView

urlpatterns = [
    path('create/', CreateTripGroupView.as_view(), name='create-trip'), #per creare un gruppo
    path('info/<group_id>/', TripGroupDetailView.as_view(), name='group-details'), #per vedere info gruppo
    path('join/<int:pk>/', JoinTripGroupView.as_view(), name='join-trip'), #per entrare nel gruppo
    path('<int:group_id>/posts/', TripGroupPostsListView.as_view(), name='group-posts'), #per avere elenco post
    path('<int:group_id>/top-like/', TopLikedPostsView.as_view(), name='group-top-liked-posts'), #per avere classifica like post
    path('<int:group_id>/top-like-user/', UserTopLikesView.as_view(), name='group-top-liked-users'), #per avere classifica like utente
    path('<int:group_id>/top-posters/', UserTopPostsView.as_view(), name='group-top-posters'), #per avere elenco poster
    path('<int:group_id>/badge/<int:user_id>/', MemberBadgeView.as_view(), name='user-group-badge'), #per avere il badge
]
