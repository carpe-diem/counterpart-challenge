# Counterpart - The Challenge (BACKEND)
> **Note**
For the development, I followed the Django-Styleguide proposed by the company [HackSoft](https://github.com/HackSoftware/Django-Styleguide).

Developers Setup
================

services with docker except the API (Django), since it is more comfortable to debug outside the container.

First, we run the services with docker, then Django.

Services with Docker (Database)
------------------------------ 
    ~$ docker-compose build
    ~$ docker-compose up -d

API
---

Environment Variables

    ~$ cp .env.example .env

Install Poetry

    ~$ curl -sSL https://install.python-poetry.org | python3 -
    ~$ export PATH="$HOME/.local/bin:$PATH"

Install dependencies

    ~$ poetry install

Run migrations

    ~$ poetry run python manage.py migrate

Run runserver

    ~$ poetry run python manage.py runserver 0.0.0.0:9000

Run tests

    ~/ poetry run python3 manage.py test