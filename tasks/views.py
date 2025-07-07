from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.utils.timezone import now
from datetime import timedelta
from .tasks import send_task_reminder
import datetime
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        if task.due_date:
            eta = task.due_date - timedelta(minutes=10)
            if eta > now():
                send_task_reminder.apply_async((task.id,), eta=eta)
class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
