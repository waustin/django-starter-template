# Django Application Starter Template

Customized Starter Django Project Starter Template

## Features

- `config/` directory to store core project files (settings, urls, wsgi)
- `apps/` directory to store application apps
- `app/core` directory to store common / core project logic not belonging to a specific app
- Django Admin for basic data Managment
- Django Ninja - REST Framework for the API

### Testing

- pytest with pytest-django and pytest-cov (coverage)
- django-test-plus
- run `pytest` command to run tests

## Steps

- Create virtualenv `python -m venv [yourenvname]`
- Activate virtualenv `source yourenvname/bin/activate`
- install inital requiremetns `pip intall -r requirements`

## TODO

- Docker and Docker compose for dev and production
- Unit / Feature Tests
- Linting
- Github Actions for linting and testing on PRs