# API Documentation for Django News App

## Overview

This Django News App provides a simple and efficient way to fetch and display news articles from the GNews API. The app supports various query parameters to filter and customize the news articles displayed. The API is designed to be RESTful and returns JSON-formatted responses.

---

## Table of Contents

1. [Endpoints](#endpoints)
    - [Home](#home)
    - [Get Articles](#get-articles)
    - [Search Articles](#search-articles)
2. [Query Parameters](#query-parameters)
3. [Responses](#responses)
4. [Error Handling](#error-handling)
5. [Caching](#caching)

---

## Endpoints

### Home

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns the home page of the application.

#### Example Request

```
GET /
```

#### Example Response

- **Status Code**: `200 OK`
- **Content**: Rendered `home.html` template.

---

### Get Articles

- **URL**: `/article`
- **Method**: `GET`
- **Description**: Fetches a list of top headlines articles based on the given query parameters.

#### Query Parameters

- `n`: Number of articles to fetch (default is 10).
- `ln`: Language of the articles (default is 'en').
- `category`: Category of the articles (default is 'general').
- `country`: Country of origin for the articles (default is 'us').

#### Example Request

```
GET /article?n=5&ln=en&category=technology&country=us
```

#### Example Response

- **Status Code**: `200 OK`
- **Content**: Rendered `article_list.html` template with a list of articles.

---

### Search Articles

- **URL**: `/search_article`
- **Method**: `GET`
- **Description**: Searches for articles based on the given query parameters.

#### Query Parameters

- `ln`: Language of the articles (default is 'en').
- `country`: Country of origin for the articles (default is 'us').
- `query`: Search query (default is an empty string).
- `max`: Maximum number of articles to return (default is 10).
- `queryBy`: Field to query by (default is "title").

#### Example Request

```
GET /search_article?ln=en&country=us&query=climate&max=5&queryBy=title
```

#### Example Response

- **Status Code**: `200 OK`
- **Content**: Rendered `article_list.html` template with a list of articles.

---

## Query Parameters

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| `n`       | Number of articles to fetch | 10 |
| `ln`      | Language of the articles | 'en' |
| `category`| Category of the articles | 'general' |
| `country` | Country of origin for the articles | 'us' |
| `query`   | Search query | '' |
| `max`     | Maximum number of articles to return | 10 |
| `queryBy` | Field to query by | 'title' |

---

## Responses

- `200 OK`: The request was successful.
- `400 Bad Request`: The request was invalid or cannot be served.
- `404 Not Found`: The requested resource could not be found.
- `500 Internal Server Error`: An error occurred on the server.

---

## Error Handling

Errors are returned as JSON objects in the following format:

```json
{
  "error": "Description of the error"
}
```

---

## Caching

Responses from the `/article` and `/search_article` endpoints are cached for 15 minutes to improve performance.

---

For more details, please refer to the source code.