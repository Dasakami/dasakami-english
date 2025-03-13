from django.http import JsonResponse
from django.shortcuts import render
from .models import Word

def game_view(request):
    return render(request, 'game/game.html')

def block_word_game(request):
    return render(request, 'game/block_word_game.html')


# views.py
from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm
import random

def word_puzzle_view(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game:word_puzzle')  # Название маршрута
    else:
        form = WordForm()

    all_words = list(Word.objects.values_list('word', flat=True))
    random.shuffle(all_words)
    selected_words = all_words[:7]  # выбираем 7 случайных

    return render(request, 'game/word_puzzle.html', {
        'form': form,
        'words': selected_words
    })


def memory_match(request):
    return render(request, 'game/memory_match.html')

def sentence_builder(request):
    return render(request, 'game/sentence_builder.html')

def flappy_word(request):
    return render(request, 'game/flappy_word.html')

def word_galaga(request):
    return render(request, 'game/word_galaga.html')

def get_word(request):
    word = Word.objects.order_by('?').first()  # Получаем случайное слово
    return JsonResponse({'word': word.word, 'translation': word.translation})
