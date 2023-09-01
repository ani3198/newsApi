from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
import requests
import json
# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# This library will be used to fetch the API.
import urllib.request

apikey = "a5867fbace87940834366d2c0acdab28"
category = "general"


@cache_page(60 * 15)  # Cache the response for 15 minutes
def get_articles(request):
    n = request.GET.get('n', 10)
    ln =  request.GET.get('ln', 'en')
    country =  request.GET.get('country', 'us')
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang={ln}&country={country}&max={n}&apikey={apikey}"
    response = requests.get(url)
    articles = response.json().get('articles', [])

    articles = response.json().get('articles', [])
    return render(request, 'article_list.html', {'articles': articles})


@cache_page(60 * 15)  # Cache the response for 15 minutes
def get_articles_by_author(request):
    author = request.GET.get('author','')
    ln =  request.GET.get('ln', 'en')
    country =  request.GET.get('country', 'us')
    query = request.GET.get('query', '')
    max_articles = request.GET.get('max', 10)
    source = request.GET.get('queryBy', "title")
    url = f"https://gnews.io/api/v4/search?q={query}&lang={ln}&country={country}&max={max_articles}&in={source}&apikey={apikey}"
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return render(request, 'article_list.html', {'articles': articles})

def home(request):
    return render(request,'home.html')