from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

PRIORITY_HIGH = 1
PRIORITY_MEDIUM = 2
PRIORITY_LOW = 3

PRIORITY_CHOICES = [
    (PRIORITY_HIGH, "Высокий приоритет"),
    (PRIORITY_MEDIUM, "Средний приоритет"),
    (PRIORITY_LOW, "Низкий приоритет"),
]

class Category(models.Model):
    slug = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    todos_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} ({self.slug})'

class Priority(models.Model):
    name = models.CharField(max_length=256)
    todos_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритеты'

    def __str__(self):
        return f'{self.name}'

class TodoItem(models.Model):
    description = models.TextField("описание")
    is_completed = models.BooleanField("выполнено", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks"
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        related_name="tasks",
        blank=True,
        null=True,
    )
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.description.lower()

    def get_absolute_url(self):
        return reverse("tasks:details", args=[self.pk])
