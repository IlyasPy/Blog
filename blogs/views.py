from django.shortcuts import render
from .serializers import BlogSerializer, ArticleSerializer
from .models import Blog, Article
from rest_framework import generics, permissions
from users.permissions import IsOwnerOrReadOnly


class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = IsOwnerOrReadOnly

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.owner,
        )


class BlogDetailView(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = IsOwnerOrReadOnly

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.owner,
        )


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = IsOwnerOrReadOnly



