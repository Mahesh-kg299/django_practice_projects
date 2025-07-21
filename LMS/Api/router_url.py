from rest_framework.routers import DefaultRouter
from .viewsets import BookViewSet\

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
url_patterns = router.urls