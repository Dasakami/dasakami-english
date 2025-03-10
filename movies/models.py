from django.db import models

class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    rating = models.FloatField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)  # Загружаемый файл
    video_url = models.URLField()  # Ссылка на видео
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='beginner')

    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.movie.title}'