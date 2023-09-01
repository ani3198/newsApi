from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article', views.get_articles, name='get_articles'),
    path('search_article', views.search_article, name='search_article'),
]