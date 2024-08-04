# Django Project Setup

``````
$ mkdir project && cd myproject
$ python3 -m venv venv-myproject
$ source venv-project/bin/activate
$ pip install django

$ (venv-project) django-admin startproject config .
$ (venv-project) python3 manage.py startapp myproject
$ (venv-project) python3 manage.py migrate
$ (venv-project) python3 manage.py runserver

```

- Add `myproject` to `config/settings.py` `INSTALLED_APPS`

