from django.shortcuts import render
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from mcc.todo.models import Todo
from mcc.todo.serializers import CreateTodoSerializer, TodoSerializer
from mcc.users.models import User


class TodoListView(generics.ListCreateAPIView):
    permissions_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = TodoSerializer

    def get_queryset(self):
        return (
            None
            if self.request.user.is_anonymous
            else Todo.objects.filter(user__email=self.request.user)
        )

    def create(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)

        request.data["user"] = User.objects.get(email=self.request.user).id
        serializer = CreateTodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "todo_id"
    permissions_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = TodoSerializer

    def get_queryset(self):
        return (
            None
            if self.request.user.is_anonymous
            else Todo.objects.filter(user__email=self.request.user)
        )
