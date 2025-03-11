from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('superadmin', 'Владыка'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')

    custom_id = models.CharField(max_length=100, null=True, blank=True, unique=False)


    def save(self, *args, **kwargs):
        if not self.custom_id:
            self.custom_id = str(self.id)  # Генерирует уникальный ID на основе стандартного id
        super().save(*args, **kwargs)



