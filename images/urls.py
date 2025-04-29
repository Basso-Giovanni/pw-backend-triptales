from django.urls import path
from .views import CreateImageView, ImageDetailView

urlpatterns = [
    path('create/', CreateImageView.as_view(), name='create-image'),
    path('<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
]
