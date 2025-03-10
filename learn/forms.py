from django import forms
from .models import PhrasalVerb
from .models import Card, Word


class PhrasalVerbForm(forms.ModelForm):
    class Meta:
        model = PhrasalVerb
        fields = ['verb', 'particle', 'translation', 'example']


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'image']

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'translation', 'transcription', 'example']

from .models import Idiom

class IdiomForm(forms.ModelForm):
    class Meta:
        model = Idiom
        fields = ['idiom', 'meaning', 'usage']