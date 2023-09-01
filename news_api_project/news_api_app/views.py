from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
import requests


import json
def getApiKey():
    with open('config.json') as f:
        config = json.load(f)
        
    api_key = config['api_key']
    return api_key



@cache_page(60 * 15)  # Cache the response for 15 minutes
def get_articles(request):
    """
    The function `get_articles` retrieves a specified number of top headlines articles from the GNews
    API based on the given parameters and returns them as a JSON response.
    
    :param request: The `request` parameter is an object that represents the HTTP request made by the
    client. It contains information such as the request method, headers, query parameters, and body
    :return: a rendered HTML template called 'article_list.html' with a context variable 'articles'
    containing a list of articles obtained from the GNews API.
    """

    n = request.GET.get('n', 10)
    ln =  request.GET.get('ln', 'en')
    category = request.GET.get('category', 'general')
    country =  request.GET.get('country', 'us')
    apikey = getApiKey()
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang={ln}&country={country}&max={n}&apikey={apikey}"
    response = requests.get(url)
    articles = response.json().get('articles', [])

    articles = response.json().get('articles', [])
    return render(request, 'article_list.html', {'articles': articles})


@cache_page(60 * 15)  # Cache the response for 15 minutes
def search_article(request):
    """
    The function `get_articles_by_author` retrieves a list of articles from the GNews API based on the
    provided query parameters and renders them in an HTML template.
    
    :param request: The `request` parameter is an object that represents the HTTP request made by the
    client. It contains information such as the request method, headers, and query parameters
    :return: a rendered HTML template called 'article_list.html' with a context variable 'articles'
    containing a list of articles obtained from the GNews API based on the provided parameters.
    """
    apikey = getApiKey()
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
    """
    The `home` function returns a rendered `home.html` template in response to a request.
    
    :param request: The request parameter is an object that represents the HTTP request made by the
    client. It contains information such as the HTTP method (GET, POST, etc.), headers, user session,
    and any data sent in the request. In this code snippet, the request object is passed to the render
    function, which
    :return: the rendered home.html template.
    """
    return render(request,'home.html')