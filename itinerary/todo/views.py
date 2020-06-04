from django.shortcuts import render
from rest_framework import generics, status

from itinerary.todo.models import Todo
from itinerary.todo.serializers import TodoSerializer


class TodoListView(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        # TODO: Return to filter by User once we figure out Auth stuff.
        return Todo.objects.all()

        # if self.request.user.is_anonymous:
        #     return None
        # return Todo.objects.filter(user=self.request.user)
