from django.db import models
from users.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)

class Task(models.Model):
    STATUS_CHOICES = [
        ('to_do', 'To Do'),
        ('going', 'Going'),
        ('done', 'Done'),
    ]
    author = models.ForeignKey(User, related_name="tasks",
                               on_delete=models.CASCADE)
    task_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="api/media/", null=True, default=None)
    text = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.task_name