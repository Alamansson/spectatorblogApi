from rest_framework import serializers
from .models import News, NewsReview


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews'] = NewsReviewSerializer(
            NewsReview.objects.filter(news=instance.id),
            many=True
        ).data
        return representation


class NewsReviewSerializer(serializers.ModelSerializer):


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




