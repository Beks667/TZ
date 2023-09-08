from rest_framework.routers import DefaultRouter
from .views import SongViewSet,SongsAlbumViewSet

router = DefaultRouter()
router.register('songs', SongViewSet, basename='songs')
router.register('songs_album', SongsAlbumViewSet, basename='songs_album')

urlpatterns = router.urls
