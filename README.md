# {{ project_name }}

## Features

* Python 3.7 and Pipenv for package managment.
* Django 2.2 LTS and Django REST Framework.
* OpenAPI 3.0 specs support and Swagger UI out of the box.
* Argon2 algo for strongest password hashing.
* Dotenv file supported.
* Docker and docker-compose files included.

## Gettting started

```bash
django-admin startproject \
    --template=https://github.com/distributed-solutions/django-openapi-project/archive/master.zip \
    --extension=py,md,env \
    myproject
```

```bash
cd myproject
mv .example.env .env
sudo pip install --upgrade pipenv
pipenv install --dev
pipenv run ./manage.py runserver
```

```bash
docker-compose up
```

## Settings

* ``SECRET_KEY`` - django's secret seed
* ``DATABASE_URL`` - database dsn (`sqlite3.db`)
* ``POSTGRES_PASSWORD`` - password for postgresql server (`postgres` by default)

## Testing

```bash
pipenv run pytest
```

## License

See [LICENSE](./LICENSE)
