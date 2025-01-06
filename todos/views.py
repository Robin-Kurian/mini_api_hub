from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from todos.models import Todo
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated


class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
