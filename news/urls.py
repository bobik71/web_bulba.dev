from django.urls import path
from . import news_views

app_name = 'news'

urlpatterns = [
    path('', news_views.news_home, name='news_home'),
    path('create', news_views.create, name='create'),
    path('<int:pk>', news_views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', news_views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', news_views.NewsDeleteView.as_view(), name='news-delete'),
]