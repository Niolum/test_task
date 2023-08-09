from rest_framework import serializers

from task.models import Task


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ['description']

    
class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at']