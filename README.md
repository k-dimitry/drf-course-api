# E-Commerce shop project using Django and DRF
This project is based on BugBytes series no [youtube.com](https://www.youtube.com/@bugbytes3923)

## Technoglogies
This project is based on the following technologies:
1. Django
2. Django REST Framework
3. DRF-Spectacular for OpenAPI schemas: swagger / redoc
4. Redis, Celery for caching

I used **uv** as package and virtual environment manager. However, it has requirements.txt for using **pip**

## Installation
```uv sync```

## Launching
1. Run redis using docker:

```docker run --name django-redis -d -p 6379:6379 --rm redis```

2. Run the server:

```python manage.py runserver```

3. Run the Celery:

```celery -A drf_course worker --loglevel=INFO```

## Credits
[BugBytes](https://www.youtube.com/@bugbytes3923), thank you again for the great course!
