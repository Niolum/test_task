from django.db import models
from django.urls import reverse


class Task(models.Model):
    """Задачи"""
    title = models.CharField('Заголовок задачи', max_length=255)
    description = models.TextField('Описание задачи')
    completed = models.BooleanField('Статус задачи', default=False)
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
    