from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .settings import MEDIA_URL, MEDIA_ROOT, DEBUG
from app.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('routers/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
