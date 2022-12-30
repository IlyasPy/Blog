from django.urls import path
from .views import BlogListView, BlogDetailView, ArticleListView, ArticleDetailView


urlpatterns = [
    path('blog-list/', BlogListView.as_view(), name='blog-list'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('articles-list/', ArticleListView.as_view(), name='articles-list'),
    path('article-detail/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]