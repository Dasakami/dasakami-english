from django.db import models

class Learn(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class PhrasalVerb(models.Model):
    verb = models.CharField(max_length=100, verbose_name="Глагол")
    particle = models.CharField(max_length=50, verbose_name="Добавление (in/out/etc)")
    translation = models.CharField(max_length=255, verbose_name="Перевод")
    example = models.TextField(verbose_name="Пример использования")

    def __str__(self):
        return f"{self.verb} {self.particle}"

# models.py


class Card(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cards/images/')
    
    def __str__(self):
        return self.title

class Word(models.Model):
    card = models.ForeignKey(Card, related_name='words', on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=200)
    transcription = models.CharField(max_length=100)
    example = models.TextField()

    def __str__(self):
        return self.word
    


class Idiom(models.Model):
    idiom = models.CharField(max_length=255)
    meaning = models.TextField()
    usage = models.TextField()

    def __str__(self):
        return self.idiom


