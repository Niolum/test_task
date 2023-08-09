from rest_framework.viewsets import ModelViewSet

from task.serializers import TaskSerializer
from task.models import Task


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()