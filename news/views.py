from urllib import request

from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import News, NewsReview
from .serializers import NewsReviewSerializer, NewsReview, NewsSerializer, NewsCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
# from account.permissions import IsActivePermission






class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]

    filterset_fields = ['blog', 'title']
    search_fields = ['title']
#
# def get_permissions(self):
#     if self.action == 'destroi':
#         return [IsAdminUser()]
#     return [IsActivePermission]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'list':
            return NewsCreateSerializer
        return NewsSerializer

    @action(['GET'], detail=True)
    def reviews(self, request, pk=None):
        news = self.get_object()
        reviews = news.reviews.all()
        serializer = NewsReviewSerializer(
            reviews, many=True
        )
        return Response(serializer.data, status=201)

class NewsReviewViewSet(ModelViewSet):
    queryset = NewsReview.objects.all()
    serializer_class = NewsReviewSerializer
    # permission_classes = [IsActivePermission]


    def get_serializer_context(self):
        return {
            'request': self.request
        }
    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args,**kwargs)