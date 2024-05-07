from django.urls import path
from rest_framework import routers
from .views import IndexView, QRInfoViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'qr_info', QRInfoViewSet)
urlpatterns = router.urls
