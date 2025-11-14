from django.shortcuts import render, HttpResponse
from .articls import articles

# Create your views here.

def article_view(request):
    return render(request, 'article/article.html', context={'articles' : articles})
    # return HttpResponse("Pages article")