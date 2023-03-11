from django.shortcuts import render

from rest_framework import generics, permissions, authentication, mixins
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from todo.models import Todo
from .serializers import TodoSerializer
from profiles.models import Profile
from .serializers import ProfileSerializer


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return self.queryset.filter(profile=self.request.user.profile)

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(profile=profile)


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return self.queryset.filter(profile=self.request.user.profile)

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(profile=profile)


class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
