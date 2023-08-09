from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from task.serializers import TaskSerializer
from task.models import Task


params = [
    openapi.Parameter("completed",
        openapi.IN_QUERY,
        description="Task status",
        type=openapi.TYPE_BOOLEAN,
        required=False
    )
]


@method_decorator(name="list", decorator=swagger_auto_schema(
    operation_description="Получить задачи (все/выполненые/невыполненные)",
    manual_parameters=params
))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(
    operation_description="Получить задачу по ее идентификатору"
))
@method_decorator(name="create", decorator=swagger_auto_schema(
    operation_description="Создать новую задачу"
))
@method_decorator(name="update", decorator=swagger_auto_schema(
    operation_description="Обновить информацию по задаче по ее идентификатору"
))
@method_decorator(name="partial_update", decorator=swagger_auto_schema(
    operation_description="Частично обновить информацию по задаче по ее идентификатору"
))
@method_decorator(name="destroy", decorator=swagger_auto_schema(
    operation_description="Удалить задачу по ее инденификатору"
))
class TaskViewSet(ModelViewSet):
    """
    Обеспечивает создание новой задачи, 
    получение одной задачи по идентификатору, 
    обновление одной задачи по идентификатору, 
    частичное_обновление задачи по идентификатору, 
    удаление одной задачи по идентификатору и 
    получение списка задач (всех, завершенных или незавершенных)
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def list(self, request, *args, **kwargs):
        completed = self.request.query_params.get('completed', None)
        if completed == None:
            queryset = Task.objects.all()
        else:
            try:
                queryset = Task.objects.filter(completed=completed)
            except ValidationError as exc:
                data = {'detail': exc}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)