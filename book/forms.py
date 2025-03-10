from django import forms
from .models import Book, Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'cover', 'level', 'description', 'file']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # Указываем поле, которое будем отображать и обрабатывать
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите ваш комментарий...'})
        }