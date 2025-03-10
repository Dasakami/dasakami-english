from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import book_list, book_detail, add_book, edit_book, delete_book
app_name = 'book'
urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('<int:book_id>/', book_detail, name='book_detail'),
    path('add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),  # Редактировать книгу
    path('books/delete/<int:book_id>/', delete_book, name='delete_book')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)