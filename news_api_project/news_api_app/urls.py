from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article', views.get_articles, name='get_articles'),
    path('articleByAuthor', views.get_articles_by_author, name='get_articles_by_author'),
    # Define more paths for other API endpoints
]