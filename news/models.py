from django.contrib.auth import get_user_model
from django.db import models
from account.models import User


class News(models.Model):
    NEWS_CATEGORY = [
        ('sport', 'Спорт'),
        ('work', 'Бизнес'),
        ('edu', 'Образование'),
    ]

    title = models.CharField(max_length=50,
                             unique=True)
    blog = models.TextField()
    images = models.ImageField(upload_to='image',
                              null=True,
                              blank=True,)

    category = models.CharField(
        max_length=15,
        choices=NEWS_CATEGORY,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['title', 'blog', 'category']

    def __str__(self):
        return self.title


# class PostImage(models.Model):
#     post = models.ForeignKey(News, on_delete=models.CASCADE,
#                              related_name='pics')
#     image = models.ImageField(upload_to='posts')


class NewsLiked(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='liked')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked',null=True,)


class NewsReview(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='reviews',)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return [self.rating,self.text]

    def __repr__(self):
        return [self.rating,self.text]


class NewsFavourites(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', null=True)


