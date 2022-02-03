from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from news.views import NewsViewSet, NewsReviewViewSet, NewsLikedViewSet
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title='blogapi',
        default_version='v1',
        description='Блог новостей'
    ),
    public=True
)


router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('reviews', NewsReviewViewSet)
router.register('like', NewsLikedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('account.urls')),
    path('api/v1/docs/', schema_view.with_ui('swagger')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


