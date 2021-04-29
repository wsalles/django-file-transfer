.PHONY: setup run

# Main variables
DOCKER_REPO := https://hub.docker.com/
IMAGE_NAME := wsalles/django-file-transfer
IMAGE_VERSION := latest

# Customizing your output
CODE_CHANGE="\\033["
WARNING := $(shell echo ${CODE_CHANGE}'33;5m')
BOLD_WARNING := $(shell echo ${CODE_CHANGE}'33;1m')
RUNNING := $(shell echo ${CODE_CHANGE}'32;5m')
SETUP := $(shell echo ${CODE_CHANGE}'36;4m')
NC := $(shell echo ${CODE_CHANGE}'0m')


check_%:
	$(eval REQ := $(shell which $* ))
	@if [ "${REQ}" = "" ]; then \
		echo "${WARNING}Please, consider doing: \n${BOLD_WARNING}make setup \n \
		      ${NC}${WARNING}\nOr just do it: \n${BOLD_WARNING}pip install $*"; \
		exit 1; \
	 fi ||:

setup:
	@echo "${SETUP}"
	@pip install -r requirements.txt

run: check_uwsgi
	@echo "${RUNNING}"
	@uwsgi --ini uwsgi.ini

dev:
	@python manage.py runserver

migrate:
	@python manage.py makemigrations
	@python manage.py migrate

superuser:
	@python manage.py createsuperuser

docker-login:
	@docker login

build:
	@docker build -t ${IMAGE_NAME}:${IMAGE_VERSION} .

push: docker-login build
	@docker push ${IMAGE_NAME}:${IMAGE_VERSION}
