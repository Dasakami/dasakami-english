from django import forms
from .models import Movie, Comment
import bleach

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Напишите комментарий...'}),
        }

    def clean_text(self):
        text = self.cleaned_data['text']
    # Очищаем теги с помощью bleach
        allowed_tags = ['b', 'i', 'u', 'em', 'strong']
        cleaned_text = bleach.clean(text, tags=allowed_tags)
    
    # Дополнительная проверка длины комментария
        if len(cleaned_text) > 1000:  # Максимальная длина комментария
            raise forms.ValidationError("Комментарий слишком длинный!")
    
        return cleaned_text