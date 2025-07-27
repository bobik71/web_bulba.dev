from django.urls import path
from . import news_views

urlpatterns = [
    path('', news_views.news_home, name='news_home'),
]