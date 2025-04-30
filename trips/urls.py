from django.urls import path
from .views import CreateTripGroupView, JoinTripGroupView, TripGroupPostsListView

urlpatterns = [
    path('create/', CreateTripGroupView.as_view(), name='create-trip'),
    path('join/<int:pk>/', JoinTripGroupView.as_view(), name='join-trip'),
    path('<int:group_id>/posts/', TripGroupPostsListView.as_view(), name='group-posts'),
]
