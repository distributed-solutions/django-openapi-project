# {{ project_name }}

## Gettting started

```bash
django-admin startproject myproject \
    --template=https://github.com/distributed-solutions/django-openapi-project/archive/master.zip
    --name=Procfile \
    --extension=py,md,env
mv  .example.env .env
```

```bash
sudo pip3 install --upgrade pip pipenv
pipenv run install --dev
pipenv run manage.py runserver
```

## Project requirements

* Python 3.7 (and pipenv)
* Django 3.0
* Django REST Framework
* Docker and docker-compose
* `.env` file supported


## Evironment

* ``SECRET_KEY`` - secret seed
* ``DATABASE_URL`` - database DSN
* ``POSTGRES_PASSWORD`` - postgresql password

## Docker
```bash
docker-compose up
```


```bash
# Build docker container
make build
# Release image
make release
```

