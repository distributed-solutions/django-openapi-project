FROM python:3.7-slim-buster

ARG BUILD_DATE
ARG VCS_REF

LABEL maintainer="osintsev@gmail.com" \
    com.microscaling.license="MIT" \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.name="{{ project_name }}" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.schema-version="1.0"

ADD . / app/
WORKDIR /app
VOLUME /app

RUN apt-get update && apt-get install --no-install-recommends -y postgresql-client openssl && \
    pip install --upgrade pip pipenv && \
    pipenv install --deploy

EXPOSE 8000

CMD /usr/bin/env pipenv run ./manage.py migrate --no-input && \
    /usr/bin/env pipenv run ./manage.py runserver 0.0.0.0:8000
