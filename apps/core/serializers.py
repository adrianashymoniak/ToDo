from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.core.models import TodoItem


class TodoItemSerializer(ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ["uuid", "title", "description", "status"]

    def create(self, validated_data):
        user = self.context.get("request").user
        if user:
            todo = TodoItem.objects.create(
                user=user,
                title=validated_data["title"],
                description=validated_data["description"],
                status=validated_data["status"],
            )
            todo.save()

            return todo


class ToDoItemOrderSerializer(Serializer):
    tasks = CharField(write_only=True, required=True)
