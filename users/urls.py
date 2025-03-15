from django.urls import path, include
from users.views import login, register, profile, logout, setting, view_profile, search_users
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views
app_name = 'users'
urlpatterns = [
    path('login/', login , name='login' ),
    path('register/', register, name='register' ),
    path('profile', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('setting/', setting, name='setting'),
    path('search/', search_users, name='search_users'),  # Страница поиска пользователей
    path('profile/<int:user_id>/', view_profile, name='view_profile'),  # Страница профиля другого пользователя
]

