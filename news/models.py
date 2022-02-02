from django.db import models



class News(models.Model):
    NEWS_CATEGORY = [
        ('SPRT', 'Спорт'),
        ('BIZNESS', 'Бизнес'),
        ('EDU', 'Образование'),
    ]

    title = models.CharField(max_length=50,
                             unique=True)
    blog = models.TextField()
    image = models.ImageField(upload_to='image',
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


class NewsReview(models.Model):
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='reviews',)
    # author = models.ForeignKey(User, on_delete=models.CASCADE,
    #                            related_name='reviews', null=True)

    text = models.TextField()
    rating = models.PositiveIntegerField(default=1, null=True, blank=True)
