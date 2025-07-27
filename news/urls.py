from django.urls import path
from . import news_views

app_name = 'news'

urlpatterns = [
    path('', news_views.news_home, name='news_home'),
]