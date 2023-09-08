from rest_framework.routers import DefaultRouter
from .views import AlbumsViewSet

router = DefaultRouter()
router.register('', AlbumsViewSet, basename='albums')
urlpatterns = router.urls
