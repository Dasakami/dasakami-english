from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Book(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=255, unique=True)  # Название книги
    cover = models.ImageField(upload_to='book/covers/', blank=True, null=True)  # Обложка
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)  # Уровень сложности
    description = models.TextField()  # Описание книги
    file = models.FileField(upload_to='book/files/')  # Файл книги (для скачивания)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.book.title}"