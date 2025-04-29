from rest_framework.routers import DefaultRouter
from .views import ImageViewSet

router = DefaultRouter()
router.register(r'', ImageViewSet)

urlpatterns = router.urls
