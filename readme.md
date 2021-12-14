# Credit Engine Solution

[Live URL](https://creditenginesolution.herokuapp.com/) : <https://creditenginesolution.herokuapp.com/>

## Modules

- Weather Module
- Users Module

## Features

- Weather Forecasting
- Responsive CSS
- Hand-written lazy scrolling
- Cached api results
- I18n support
- Model factories
- Python type hinting
- Easy setup/deployment

## Usage

### Dependencies

- Redis
- Python Memcahced

The listed dependencies above are needed to run the application.

Please refer to these links to install the dependencies:

- Redis: <https://redis.io/topics/quickstart>
- Python Memcahced: <https://pypi.org/project/python-memcached/>

### Method 1: Using Poetry

To use this template, first ensure that you have
[Poetry](https://python-poetry.org/docs/) available.

After that, you should:

1. Install the requirements of the project template by running
    ```
    poetry install
    ```
2. Run the project
    ```
    poetry run python manage.py runserver
    ```


It will ask you a few questions, e.g. project's name.
To create isomorphic single-page application set `frontend_style == spa`. Then separate node application will be created supported by [Razzle](https://razzlejs.org/)

After generation completes, **you should deactivate virtual environment for cookiecutter**,
search for any TODOs in the code and make appropriate changes where needed.

See README.md in the generated project for instructions on how to set up your development environment.


## Different frontend styles

### SPA

Isomorphic Javascript single-page application rendered with node and backed by Django Rest Framework. Enabled with `frontend_style == spa`.
During development and production separate node container is used to run and serve assets if needed.
Translations are done with [i18next](https://www.i18next.com/) and its companion library for React.

### Webapp

React powered application rendered with Django templates. This is the default option. Enabled with `frontend_style == webapp`.
During development separate container is used to build assets. In production, node built with multi-stage image.
Translations are done with Django JavaScriptCatalog.


## Upgrading project template

First ensure you have a python3 interpreter with `cookiecutter` installed.

To upgrade an existing project, change the current working directory to the root of the project you want to upgrade. i.e. `cd project-to-upgrade`. Ensure your have not checked out the `template` branch.

Then run `python ~/path/to/django-project-template/upgrade-template.py`

This will make a commit to the branch `template` in your project with the updates to the project template. Then merge the `template` branch.

## Applying codemods

First activate Python 3 interpreter with required dependencies and ensure `docker` is installed and working.

Change the current working directory to the root of the project you want to apply codemods for. i.e. `cd project-to-upgrade`.

Then run `python ~/path/to/django-project-template/upgrade-template.py --apply-frontend-codemods`

This will build custom docker image to update old frontend versions.

## Docker images

The template uses our own images for CI runs. One for the template itself and a second one
for generated projects. Both images are alpine based and contain python3, pip and some support
packages. The images are published to [repository container registry](https://gitlab.com/thorgate-public/django-project-template/container_registry) and also to [docker hub](https://hub.docker.com/u/thorgate).

The images are built in CI (from default branches only) and also updated every day via schedules.

**Project CI Image**

- [Dockerfile-ci](./utils/Dockerfile-ci)
- Image in repository registry: `registry.gitlab.com/thorgate-public/django-project-template/ci`
- Image in docker hub: `thorgate/django-template-ci`
  - [see online](https://hub.docker.com/r/thorgate/django-template-ci)

**Template CI Image:**

- [Dockerfile-base-ci](./utils/Dockerfile-base-ci)
- Image in repository registry: `registry.gitlab.com/thorgate-public/django-project-template/base-ci`
- Image in docker hub: `thorgate/django-template-base-ci`
  - [see online](https://hub.docker.com/r/thorgate/django-template-base-ci)
