from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',
                  'completed', 'due_date', 'created_at']
        read_only_fields = ['user', 'created_at']
