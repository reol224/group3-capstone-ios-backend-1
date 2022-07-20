# Django backend boilerplate for GIS development

## Use this boilerplate

Clone to a new repo, and start work on that repo

## Developing in container

### requirements:

* Linux/MacOS/Windows installed
* Docker installed

### Start the development container while using MacOS / Linux

1. start the backend container: `./dev backend`

### Start the development container in Windows

1. run `.\dev.bat backend` to start and enter the backend container

### Start dev-server in development container

1. run `./dev initdir` to create directories and log file
1. install dependencies: `poetry install` (Only first time or after git-pull)
1. start django server: `./dev run`

create a super user:

`poetry run python3 manage.py createsuperuser`

### access the dev-site:

* backend: http://localhost:8000/
* DRF interface: http://localhost:8000/api

### Other commands:

* Install new pip package: `poetry add <package-name>`
* Create database migrations: `./dev makemigrations`
* Migrate the dev-database: `./dev migrate`
* Run Django test: `./dev test`
* Run Coverage: `./dev coverage`
* Create i18n .po file: `./dev mkmsg`
* Complie i18n .po file to .mo file: `./dev comsg`

### drop off all containers

* for Windows: `.\dev.bat down` 
* for MacOS and Linux`./dev down`

## about poetry:

* install dependency: `poetry add pendulum`
* run script: `poetry run python3 xxxxx.py`
* remove a dependency: `poetry remove pendulum`
* delete cache for a source `rm -rf ~/.cache/pypoetry/cache/repositories/tengxun/`