
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from news.views import NewsViewSet, NewsReviewViewSet

router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('reviews', NewsReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
