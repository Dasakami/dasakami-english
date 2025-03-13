from django.urls import path
from . import views
app_name = 'game'
urlpatterns = [
    path('', views.game_view, name='game'),
    path('get-word', views.get_word, name='get_word'),
    path('block_word_game/', views.block_word_game, name='block_word_game'),
    path('word_puzzle/', views.word_puzzle_view, name='word_puzzle'),
    path('memory_match/', views.memory_match, name='memory_match'),
    path('sentence_builder/', views.sentence_builder, name='sentence_builder'),
    path('flappy_word/', views.flappy_word, name='flappy_word'),
    path('word_galaga/', views.word_galaga, name='word_galaga'),
]