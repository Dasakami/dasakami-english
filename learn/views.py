from django.shortcuts import render, redirect
from .models import Learn
from django.shortcuts import render, get_object_or_404
from .models import PhrasalVerb
from .forms import PhrasalVerbForm
from .models import Card, Word
from .forms import CardForm, WordForm
from .models import Idiom
from .forms import IdiomForm

def phrases_verbs_view(request):
    verbs = PhrasalVerb.objects.all()
    form = PhrasalVerbForm()

    if request.method == 'POST':
        form = PhrasalVerbForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learn:phrases_verbs')

    return render(request, 'learn/phrases_verbs.html', {'verbs': verbs, 'form': form})

def delete_phrasal_verb(request, pk):
    verb = get_object_or_404(PhrasalVerb, pk=pk)
    verb.delete()
    return redirect('learn:phrases_verbs')


# Страница с карточками
def words_view(request):
    cards = Card.objects.all()
    return render(request, 'learn/words.html', {'cards': cards})

def create_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save()
            # После сохранения карточки перенаправляем обратно на эту же страницу, чтобы отобразить карточку
            return render(request, 'learn/create_card.html', {'form': form, 'card': card})
    else:
        form = CardForm()
    return render(request, 'learn/create_card.html', {'form': form})
# Страница карточки с таблицей слов
def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    words = Word.objects.filter(card=card)
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.card = card
            word.save()
            return redirect('learn:card_detail', card_id=card.id)
    else:
        form = WordForm()
    return render(request, 'learn/card_detail.html', {'card': card, 'words': words, 'form': form})

# Удаление карточки
def delete_card(request, card_id):
    card = Card.objects.get(id=card_id)
    card.delete()
    return redirect('learn:words')

# Удаление слова
def delete_word(request, word_id):
    word = Word.objects.get(id=word_id)
    word.delete()
    return redirect('learn:card_detail', card_id=word.card.id)


def learn(request):
    categories = Learn.objects.all()
    return render(request, 'learn/learn.html', {'categories': categories})


def words(request):
    return render(request, 'learn/words.html')

def phrases(request):
    return render(request, 'learn/phrases.html')

def grammar(request):
    return render(request, 'learn/grammar.html')




# Отображение списка идиом
def idioms_list(request):
    idioms = Idiom.objects.all()
    return render(request, 'learn/idioms_list.html', {'idioms': idioms})

# Добавление новой идиомы
def add_idiom(request):
    if request.method == 'POST':
        form = IdiomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learn:idioms_list')
    else:
        form = IdiomForm()
    return render(request, 'learn/add_idiom.html', {'form': form})

# Удаление идиомы
def delete_idiom(request, idiom_id):
    idiom = Idiom.objects.get(id=idiom_id)
    idiom.delete()
    return redirect('learn:idioms_list')

def youtube(request):
    return render (request, 'learn/youtube.html')


