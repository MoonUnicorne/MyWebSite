from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Article 
from .forms import ArticleForm


def articles_view(request):
    articles = Article.objects.all().order_by("-datePublication")

    return render(request, 'articles/articles.html', context={'articles' : articles})

def articles_view_ordered(request, order):
    try:
        if order == 1:
            articles = Article.objects.all().order_by("-datePublication")
        elif order == 2:
            articles = Article.objects.all().order_by("datePublication")
        elif order == 3:
            articles = Article.objects.all().order_by("titre")
        elif order == 4:
            articles = Article.objects.all().order_by("-titre")
        else:
            articles = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404("Articles non trouver")
    return render(request, 'articles/articles.html', context={'articles' : articles})

def article_view(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        raise Http404("Article non trouver")
    return render(request, 'articles/article.html', context={'article' : article})

def create_article_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        form.save()
        # return HttpResponseRedirect('/articles/')
        return HttpResponseRedirect(reverse('articles:Articles'))
    return render(request, 'articles/create_article.html', context={'form': ArticleForm()})