from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import CommentForm
from .forms import BookForm


def book_list(request):
    query = request.GET.get('q', '')  # Получаем поисковый запрос
    level = request.GET.get('level', '')  # Получаем уровень книги

    book = Book.objects.all()

    if query:
        book = book.filter(title__icontains=query)  # Фильтруем по названию

    if level:
        book = book.filter(level=level)  # Фильтруем по уровню

    return render(request, 'book/book_list.html', {'book': book})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    recommended_books = Book.objects.exclude(id=book_id).order_by('?')[:5]  # Исключаем текущую книгу
    comments = book.comments.all()  # Получаем все комментарии к книге
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.book = book
            comment.save()
            return redirect('book:book_detail', book_id=book.id)  # Перезагружаем страницу, чтобы показать новый комментарий
    else:
        form = CommentForm()

    return render(request, 'book/book_detail.html', {'book': book, 'comments': comments, 'form': form, 'recommended_books': recommended_books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('book:book_list')
    else:
        form = BookForm()
    return render(request, 'book/add_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('book:book_list')  # Перенаправление обратно на список книг

    return render(request, 'book/book_confirm_delete.html', {'book': book})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')  # Перенаправление на список книг
    else:
        form = BookForm(instance=book)

    return render(request, 'book/edit_book.html', {'form': form})
