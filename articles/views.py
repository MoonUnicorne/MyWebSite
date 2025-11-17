from django.shortcuts import render, HttpResponse
# from .articls import articles

from .models import Article

# Create your views here.

def articles_view(request):
    articles = Article.objects.all().order_by("-datePublication")

    return render(request, 'articles/articles.html', context={'articles' : articles})
    # return HttpResponse("Pages article")

def article_view(request, slug):
    # for article in articles:
    #     if article["slug"] == slug:
    #         # return HttpResponse(f"Titre : {article["titre"]}\nContenu : {article["contenu"]}")
    #         return render(request, 'articles/article.html', context={'article' : article})
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article.html', context={'article' : article})
    # return HttpResponse(f"Article {slug} non trouver")