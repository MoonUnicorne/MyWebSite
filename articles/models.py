from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    contenu = models.TextField()
    datePublication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre