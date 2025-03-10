from django import forms
from django.forms import modelformset_factory
from .models import Flashcard

# Определим форму для одной карточки
class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['word', 'translation', 'image']

