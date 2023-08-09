from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from task.serializers import TaskSerializer
from task.models import Task


class TaskViewSet(ModelViewSet):
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