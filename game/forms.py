# forms.py
from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word']
        widgets = {
            'word': forms.TextInput(attrs={'placeholder': 'Введите слово', 'class': 'word-input'})
        }
