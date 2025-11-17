from django.shortcuts import render
from django.http import Http404

from .models import Article


def articles_view(request):
    articles = Article.objects.all().order_by("-datePublication")

    return render(request, 'articles/articles.html', context={'articles' : articles})

def article_view(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        raise Http404("Article non trouver")
    return render(request, 'articles/article.html', context={'article' : article})

def create_article_view(request):
    return render(request, 'articles/create_article.html')