from django.urls import path, include
from rest_framework.routers import SimpleRouter

from task.views import TaskViewSet



router_task = SimpleRouter()
router_task.register('task', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router_task.urls))
]