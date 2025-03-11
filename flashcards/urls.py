# flashcards/urls.py
from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', views.flashcard_list, name='flashcard_list'),
    path('create/', views.flashcard_create, name='flashcard_create'),
    path('flashcard/<int:pk>/add_wordcards/', views.add_wordcards, name='add_wordcards'),
     path('<int:pk>/delete/', views.flashcard_delete, name='flashcard_delete'),
    path('<int:pk>/', views.flashcard_detail, name='flashcard_detail'),
    path('<int:pk>/import-pdf/', views.import_wordcards_pdf, name='import_wordcards_pdf'),

]
