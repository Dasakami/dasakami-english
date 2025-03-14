# flashcards/models.py
from django.db import models

class Flashcard(models.Model):
    word = models.CharField(max_length=100)  # слово на английском
    translation = models.CharField(max_length=100)  # перевод слова
    image = models.ImageField(upload_to='flashcards/images/')  # изображение
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания

    def __str__(self):
        return f'{self.word} - {self.translation}'

class WordCard(models.Model):
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE, related_name='wordcards')
    word_en = models.CharField(max_length=100)
    word_ru = models.CharField(max_length=100)
    image = models.ImageField(upload_to='word_images/', blank=True, null=True)