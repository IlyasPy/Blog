from django.shortcuts import render
from rest_framework import permissions, mixins, generics
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from .models import CustomUser
from .permissions import IsOwnerOrReadOnly


class RegisterAPIView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully."
        })


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

