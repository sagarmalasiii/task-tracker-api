from celery import shared_task
from django.core.mail import send_mail
from .models import Task

@shared_task
def send_task_reminder(task_id):
    try:
        task = Task.objects.get(id=task_id)
        send_mail(
            subject=f"Reminder: {task.title}",
            message=f"Don't forget: {task.description or 'No details'}\nDue: {task.due_date}",
            from_email=None,
            recipient_list=["recipient@example.com"],  # Replace or pass dynamically
        )
        return f"Reminder sent for task {task.title}"
    except Task.DoesNotExist:
        return "Task not found"
