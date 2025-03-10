# flashcards/urls.py
from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', views.flashcard_list, name='flashcard_list'),
    path('create/', views.flashcard_create, name='flashcard_create'),
    path('<int:pk>/', views.flashcard_detail, name='flashcard_detail'),
]
