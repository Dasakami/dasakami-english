# views.py
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from .forms import CommentForm

# Страница с фильмами
# views.py
from django.shortcuts import render
from .models import Movie

def movie_list(request):
    level = request.GET.get('level', None)  # Получаем параметр уровня из URL
    search_query = request.GET.get('q', '')# Получаем запрос на поиск

    # Фильтрация по уровню сложности
    if level and level in dict(Movie.CATEGORY_CHOICES).keys():  
        movies = Movie.objects.filter(category=level)
    else:
        movies = Movie.objects.all()

    # Фильтрация по запросу поиска
    if search_query:
        movies = Movie.objects.filter(title__icontains=search_query)
    else:
        movies = Movie.objects.all()  # Ищем по названию (игнорируя регистр)

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'search_query': search_query,  # Передаем запрос поиска в шаблон
    })


# Страница добавления фильма
def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)  # Добавляем request.FILES для загрузки файла
        if form.is_valid():
            form.save()
            return redirect('movies:movie_list')  # Меняем на правильный маршрут
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    recommended_movies = Movie.objects.exclude(pk=pk).order_by('?')[:5] 
    comments = movie.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return redirect('movies:movie_detail', pk=movie.pk)  # Используй pk
    else:
        form = CommentForm()

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'comments': comments,
        'form': form,
        'recommended_movies': recommended_movies,
    })



def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:movie_detail', pk=movie.id)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/edit_movie.html', {'form': form, 'movie': movie})

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movies:movie_list')  # Перенаправление после удаления

