from rest_framework import serializers
from .models import News, NewsReview, NewsLiked


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

    def validate_news(self, news):
        if self.Meta.model.objects.filter(news=news).exists():
            raise serializers.ValidationError(
                "Вы уже оставляли коммент на эту статью"
            )
        return news

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError(
                "Рейтинг должен быть от 1 до 5"
            )
        return rating

    def create(self, validated_data):
        user =self.context.get('request').user
        validated_data['name'] = user
        review = NewsReview.objects.create(**validated_data)
        return review


class NewsLikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLiked
        fields = "__all__"


    def validate_news(self, news):
        if self.Meta.model.objects.filter(news=news).exists():
            self.Meta.model.objects.filter(news=news).delete()
            raise serializers.ValidationError("Вы успешно сняли лайк")
        return news

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        like = NewsLiked.objects.create(**validated_data)
        return like







