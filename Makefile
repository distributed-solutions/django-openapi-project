PROJECT_NAME := {{ project_name }}-backend
DOCKER_IMAGES := registry.gitlab.com/distributed-solutions/$(PROJECT_NAME) \
	registry.heroku.com/{{ project_name }}/web

default: build

build:
	@docker build -t $(PROJECT_NAME) .
	$(foreach IMAGE,$(DOCKER_IMAGES),$(shell docker tag $(PROJECT_NAME) $(IMAGE)))

release:
	$(foreach IMAGE,$(DOCKER_IMAGES),$(shell docker push $(IMAGE)))

migrate:
	@pipenv run ./manage.py makemigrations --no-input
	@pipenv run ./manage.py migrate --no-input

.PHONY: default build release migrate
