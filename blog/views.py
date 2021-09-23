from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404


def all_articles(request):
    obj = Article.published.all()
    return render(request, 'blog/all_articles.html', context={'obj': obj})


def article_detail(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/article.html', context={'article': article})
