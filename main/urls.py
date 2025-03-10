from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('', views.home, name='home' ),
    path('app/', views.app, name='app' ),
    path('accounts/', include('allauth.urls')),
    path('open-admin/', views.open_admin, name='admin'),
    path('learn/', include(('learn.urls'), namespace='learn')),
    path('users/', include(('users.urls'), namespace='users')),
    path('book/', include(('book.urls'), namespace='book')),
    path('movies/', include(('movies.urls'), namespace='movies')),
    path('flashcards/', include(('flashcards.urls'), namespace='flashcards')),
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)