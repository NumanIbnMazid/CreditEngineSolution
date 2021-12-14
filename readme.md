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

### Method 2: Using Pip

To use this template, first ensure that you have
[Poetry](https://python-poetry.org/docs/) available.

After that, you should:

1. Create a python virtual environment and run the following
    ```
    pip install -r requirements.txt
    ```
2. Run the project
    ```
    python manage.py runserver
    ```