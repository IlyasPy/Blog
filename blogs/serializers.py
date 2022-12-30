from rest_framework import serializers
from .models import Blog, Article


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'name', 'description', 'owner', 'date_added']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'blog', 'title', 'article_text', 'date_added']

