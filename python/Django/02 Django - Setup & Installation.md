---
title: "Django Installation & Setup"
author:
	- Devin Schumacher
...
# Django Installation & Setup
To install & use Django, there are a few pre-requisites that you need:
1. python 3
2. pip
3. a virtual environment (venv)


## Python
If you don't know if you have python or not - you probably shouldnt even be reading about Django yet. 

But anyways…

Check your version of python with 

```python
python --version
```

## PIP

Django is a python package, so we use `pip` to install it. 

You can check your PIP version with:

```python
pip --version
```

## Virtual Environment

Highly recommend to have a dedicated venv for each Django project (all projects really).

Virtual environments hold your project and all the imports & installations in it's own "environement" to prevent conflicts with other projects on your machine.

When you're inside of your project directory, create a virtual environment with:

```python
python3 -m venv venv
```
Once the `venv` is created, you can activate it by running:

```python
source venv/bin/activate
```

Personally, I just set this up as an autocomplete text snippet with Dash - because you have to use it so much.

When I type `@venv:` my text autocompletes this command:

```python
python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip 
```

## Installing Django

Time to install Django. Install Django (with pip) with this command:

```python
python3 -m pip install Django
```

### Checking your Django installation

To check your Django installation & version, run:

`django-admin --version`


## Setting up your Django Project

In your project folder, run this command to start

```python
django-admin startproject project_django .
```
*Note: you can replace `project_django` with whatever you want the name of your project to be.*

You will see a new directory has been created with the following file structure:

```
├── project_django
│   ├── __init__.py
|   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── .venv/
```


### Directory structure

The `.venv` directory was created with our virtual environment but Django has added a `project_django` directory and a `manage.py` file. 

**Within `project_django` are five new files:**

1. `__init__.py` - indicates that the files in the folder are part of a Python package. Without this file, we cannot import files from another directory.
2. `asgi.py` allows for an optional [Asynchronous Server Gateway Interface](https://asgi.readthedocs.io/en/latest/specs/main.html) to be run
3. `settings.py` controls our Django project’s overall settings
4. `urls.py` tells Django which pages to build in response to a browser or URL request
5. `wsgi.py` stands for [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) which helps Django serve our eventual web pages.

* `manage.py` file is not part of `django_project` but is used to execute various Django commands such as running the local web server or creating a new app.

### Run Django

Inside your `project_name` directory, run the following command to have Django spin up a development (local) server.

```python
python3 manage.py runserver
```

You'll be able to access the live version of your project in your browser by typing either of the following:

`127.0.0.1:8000` or `localhost:8000`

Error?!

If you see the following error, you will need to stop the server, and run the command you see in the terminal.

![django run error.png](/Users/devin/Articles/images/django run error.png)

So I needed to kill my server, and run: 

```
python manage.py migrate
```

Then restart it with:

```
python3 manage.py runserver
```

And now when i go to `127.0.0.1:8000` I see this:

![django with debug TRUE.png](../images/django with debug TRUE.png "django with debug TRUE.png")

What Django has done here is create a SQLite database and migrated its built-in apps provided for us. 

This is represented by the new file `db.sqlite3` in our directly.



