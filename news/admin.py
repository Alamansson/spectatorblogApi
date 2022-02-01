
from django.contrib import admin

# Register your models here.
from news.models import News, NewsReview

admin.site.register(News)
admin.site.register(NewsReview)