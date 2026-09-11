from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<slug:slug>/', views.game_detail, name='game_detail'),
    path('gallery/', views.gallery, name='gallery'),
]
