from django.urls import path
from .views import CreateTripGroupView, JoinTripGroupView

urlpatterns = [
    path('create/', CreateTripGroupView.as_view(), name='create-trip'),
    path('join/<int:pk>/', JoinTripGroupView.as_view(), name='join-trip'),
]
