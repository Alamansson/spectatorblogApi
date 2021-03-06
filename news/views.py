from rest_framework.viewsets import ModelViewSet
from .models import News, NewsLiked, NewsFavourites
from .serializers import NewsReviewSerializer, NewsReview, NewsSerializer, \
    NewsCreateSerializer, NewsUpdateSerializer, NewsLikedSerializer, NewsFavouriteSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from account.permissions import IsActivePermission
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser



class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer = NewsSerializer
    permission_classes = [IsActivePermission]



    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]

    filterset_fields = ['category']
    search_fields = ['title', 'blog']


    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'list':
            return NewsCreateSerializer
        elif self.action == 'destroi':
            return [IsAdminUser()]
        return NewsSerializer

    @action(['GET'], detail=True)
    def reviews(self, request, pk=None):
        news = self.get_object()
        reviews = news.reviews.all()
        serializer = NewsReviewSerializer(
            reviews, many=True
        )
        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = NewsUpdateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        data = serializer.data
        if data.get('title', False):
            instance.title = data.get('title')

        instance.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewsLikedViewSet(ModelViewSet):
    queryset = NewsLiked.objects.all()
    serializer_class = NewsLikedSerializer
    permission_classes = [IsActivePermission]


class NewsReviewViewSet(ModelViewSet):
    queryset = NewsReview.objects.all()
    serializer_class = NewsReviewSerializer
    permission_classes = [IsActivePermission]

    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args,**kwargs)


class NewsFavouriteViewSet(ModelViewSet):
    queryset = NewsFavourites.objects.all()
    serializer_class = NewsFavouriteSerializer
    permission_classes = [IsActivePermission]

