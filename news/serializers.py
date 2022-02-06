from rest_framework import serializers

from account.permissions import IsActivePermission
from .models import News, NewsReview, NewsLiked, NewsFavourites
from rest_framework.response import Response
from rest_framework import status


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'


class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title']


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsReviewSerializer(serializers.ModelSerializer):
    news_title = serializers.SerializerMethodField("get_news_title")

    class Meta:
        model = NewsReview
        fields = '__all__'

    def get_news_title(self, news_review):
        title = news_review.news.title
        return title

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError(
                "Рейтинг должен быть от 1 до 5"
            )
        rating = (self.Meta.model().rating + rating)/2
        return rating

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        review = NewsReview.objects.create(**validated_data)
        return review


class NewsLikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLiked
        fields = "__all__"

    def validate_news(self, news):
        if self.Meta.model.objects.filter(news=news).exists():
            self.Meta.model.objects.filter(news=news).delete()
            raise serializers.ValidationError("Вы сняли лайк")
        return news

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        like = NewsLiked.objects.create(**validated_data)
        return like


class NewsFavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsFavourites
        fields = "__all__"

    def validate_news(self, news):
        if self.Meta.model.objects.filter(news=news).exists():
            self.Meta.model.objects.filter(news=news).delete()
            raise serializers.ValidationError("Вы убрали с избранного")
        return news

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        favourite = NewsFavourites.objects.create(**validated_data)
        return favourite









