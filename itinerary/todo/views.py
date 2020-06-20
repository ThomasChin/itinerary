from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response


from itinerary.todo.models import Todo
from itinerary.todo.serializers import CreateTodoSerializer, TodoSerializer
from itinerary.users.models import User


class TodoListView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        # TODO: Return to filter by User once we figure out Auth stuff.
        return Todo.objects.all()

        # if self.request.user.is_anonymous:
        #     return None
        # return Todo.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # TODO: Filter by user once User System is implemented.
        request.data["user"] = User.objects.get(email="tchin10@outlook.com").id
        serializer = CreateTodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)
