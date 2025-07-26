from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),       # главная страница на корневой URL
    path('about/', views.about, name='about')
]


