from django.urls import path
from .views import *

urlpatterns = [
    path('', AnimeView.as_view(), name='anime_list'),
    path('<slug:slug>/', AnimeDetailView.as_view(), name='anime_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('character/<str:slug>/', CharacterView.as_view(), name='character_detail'),
]