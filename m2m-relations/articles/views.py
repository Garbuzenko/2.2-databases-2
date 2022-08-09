from django.shortcuts import render
import json
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all()
    # a = Article.articles.all()
    # for article in articles:
        # print(article.articles.all())
        # article.tags_set.add():
        # for tag in article.tags.all():
        #     print(tag)

    context = {"articles": articles}


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
