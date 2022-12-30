from django.urls import path
from .views import RegisterAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='registration'),
    path('users-list/', UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]