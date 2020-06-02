from rest_framework.serializers import ModelSerializer

from itinerary.todo.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ("description", "notes", "deadline")
