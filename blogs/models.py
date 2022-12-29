from django.db import models
from users.models import CustomUser


class Blog(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_owner')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return f'{self.owner} - {self.name}'


class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    article_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f'{self.author} + {self.title}'
