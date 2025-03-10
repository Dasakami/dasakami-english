# flashcards/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Flashcard
from .forms import FlashcardForm

def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcards/flashcard_list.html', {'flashcards': flashcards})

def flashcard_create(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('flashcards:flashcard_list')
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/flashcard_create.html', {'form': form})

def flashcard_detail(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)
    return render(request, 'flashcards/flashcard_detail.html', {'flashcard': flashcard})
