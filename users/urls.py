from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import UserProfileView, UpdateProfileView, RegisterUserView, LoginUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='update-profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
