from django import forms
from django.forms import modelformset_factory
from .models import Flashcard

from .models import WordCard
from django.forms import modelformset_factory

# Определим форму для одной карточки
class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['word', 'translation', 'image']


class WordCardForm(forms.ModelForm):
    class Meta:
        model = WordCard
        fields = ['word_en', 'word_ru', 'image']

WordCardFormSet = modelformset_factory(
    WordCard,
    form=WordCardForm,
    extra=10,  # Можно 10 сразу показать, можно изменить
    can_delete=False
)
