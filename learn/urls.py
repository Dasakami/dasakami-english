from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'learn'

urlpatterns = [
    path('', views.learn, name='learn'),
    path('phrases/', views.phrases, name='phrases'),
    path('grammar/', views.grammar, name='grammar'),
    path('phrases_verbs/', views.phrases_verbs_view, name='phrases_verbs'),
    path('phrases_verbs/delete/<int:pk>/', views.delete_phrasal_verb, name='delete_phrasal_verb'),
    path('words/', views.words_view, name='words'),  # Страница со всеми карточками
    path('create_card/', views.create_card, name='create_card'),
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
    path('delete_card/<int:card_id>/', views.delete_card, name='delete_card'),
    path('delete_word/<int:word_id>/', views.delete_word, name='delete_word'),
    path('idioms_list/', views.idioms_list, name='idioms_list'),
    path('add/', views.add_idiom, name='add_idiom'),
    path('delete/<int:idiom_id>/', views.delete_idiom, name='delete_idiom'),
    path('youtube/', views.youtube, name='youtube'),
    path('card/<int:card_id>/import/', views.import_words, name='import_words'),

]
if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
