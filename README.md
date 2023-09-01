# newsApi

Certainly! Below is a sample `README.md` file for your Django News App project.

---

# Django News App

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Caching](#caching)


## Overview

Django News App is a web application built with Django that fetches and displays news articles from the GNews API. The application supports various query parameters to filter and customize the news articles displayed.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x
- pip

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/django-news-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django-news-app
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

5. Open your browser and go to `http://localhost:8000/`.

## Usage

- To view the home page, navigate to `/`.
- To fetch top headlines, navigate to `/article`.
- To search for articles, navigate to `/search_article`.

## API Documentation

For detailed API documentation, please refer to the [API Documentation](News_Api_Doc.md) file.

## Caching

The application uses Django's caching mechanism to cache responses from the `/article` and `/search_article` endpoints for 15 minutes.

