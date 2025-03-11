# flashcards/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Flashcard, WordCard
from .forms import WordCardFormSet
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



def flashcard_delete(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)
    if request.method == 'POST':
        flashcard.delete()
        return redirect('flashcards:flashcard_list')
    return render(request, 'flashcards/flashcard_confirm_delete.html', {'flashcard': flashcard})

def add_wordcards(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)
    if request.method == 'POST':
        formset = WordCardFormSet(request.POST, request.FILES, queryset=WordCard.objects.none())
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.flashcard = flashcard
                instance.save()
            return redirect('flashcards:flashcard_detail', pk=flashcard.pk)
    else:
        formset = WordCardFormSet(queryset=WordCard.objects.none())
    return render(request, 'flashcards/add_wordcards.html', {
        'flashcard': flashcard,
        'formset': formset
    })

import fitz  # PyMuPDF
from django.core.files.storage import default_storage

def import_wordcards_pdf(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)

    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']

        # Сохраняем файл временно
        file_path = default_storage.save('temp_uploaded.pdf', pdf_file)
        full_path = default_storage.path(file_path)

        # Читаем содержимое PDF
        doc = fitz.open(full_path)
        text = ''
        for page in doc:
            text += page.get_text()

        doc.close()

        # Удаляем временный файл
        default_storage.delete(file_path)

        # Обработка строк (разделение по строкам)
        lines = text.splitlines()
        for line in lines:
            if '-' in line:
                parts = line.split('-', 1)
            elif ':' in line:
                parts = line.split(':', 1)
            else:
                continue  # если нет разделителя

            word = parts[0].strip()
            translation = parts[1].strip()

            if word and translation:
                WordCard.objects.create(
    flashcard=flashcard,
    word_en=word,
    word_ru=translation
)


        return redirect('flashcards:flashcard_detail', pk=flashcard.pk)

    return render(request, 'flashcards/import_wordcards_pdf.html', {'flashcard': flashcard})
