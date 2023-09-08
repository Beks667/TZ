from rest_framework.routers import DefaultRouter
from .views import ExecutorViewSet

router = DefaultRouter()
router.register('', ExecutorViewSet, basename='singer')
urlpatterns = router.urls
