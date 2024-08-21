from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import TaskSerializer, ProjectSerializer
from .models import Task, Project
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)