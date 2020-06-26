from rest_framework.fields import BooleanField, CharField, DateTimeField, IntegerField
from rest_framework.serializers import ModelSerializer, Serializer

from mcc.todo.models import Todo
from mcc.users.models import User


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "description", "notes", "deadline", "done")


class CreateTodoSerializer(Serializer):
    description = CharField()
    notes = CharField(allow_blank=True)
    deadline = DateTimeField(required=False, allow_null=True)
    done = BooleanField(default=False)
    user = IntegerField()

    def create(self, validated_data):
        todo = Todo(
            description=validated_data["description"],
            notes=validated_data["notes"],
            deadline=validated_data["deadline"],
            done=validated_data["done"],
            user=User.objects.get(id=validated_data["user"]),
        )
        todo.save()
        return todo
