# S01N02 Django Initialization

## Introduction

- third-party-solution

* versatile, highly customizable, 
* comprehensive: got everything you need for a web app
* low maintenance: one guy build a pro-like web app
* compatiable with React and Angular
* used to power Instagram and other larger product

- build projects

* Model View Controller model
* client: web browser or API request
* app: url dispatcher invokes some function to do something, e.g. yelp.com/new-york/restaurant
* database: store information

- app fetches data from database (model)
- app (controller) manipulates the data into view
- app sends HTML or JSON (view) to client

* environment or package with bunch of library

## Setting Up An Environment

### Code

```bash
# make directory
mkdir

# create virtual environment
virtualenv venv

# activate virtual environment
source venv/bin/activate

# install python packages, django, for backend
pip install django

# install python packages, django, for images
pip install pillow (for python images)

# list all packages and write to "requirements.tsx"
pip freeze > requirements.txt
```

### Note

- install virtual environment once per new project
- close the door to the framework, django
- activate virtualenv
- have same version of library when git or sharing e.g. 5.1.3
- download Python extensions on virutal studio code
- django-admin is modular, many apps under one project
- myfirstproject/myfirstproject > core > settings
- new computer, new virutal environment

## Starting A Project

### Code

```bash
# create a project using commend, django-admin
django-admin startproject

# create database on pre-installed app to store users
python manage.py migrate

# create super users
python manage.py createsuperuser
```

### Note

#### `project/core/__init__.py` 

- in the core is usually empty
- create module with __init__
- parse different parts of url 
- request from asgi.py or wsgi.py are redirected to urls.py
- asgi and wsgi are entry points

#### `project/core/settings.py`

- SECRET_KEY is stored at global environment
- DEBUG should be changed to False in production
- ALLOWED_HOSTS lists domain name or ip address
- INSTALLED_APPS manages 
- MIDDLEWARE manages requests
- TEMPLATES is html page
- TEMPLATES[0]["DIRS"] global page like entry
- TEMPLATES[0]["DIRS"] specific page like admin?
- DATABASES has built-in sqlite3, usually progresql
- DATABASES, unless old databases
- AUTH_PASSWORD_VALIDATORS, have cap letter
- STATIC_URL is usually changed in production mode
- DEFAULT_AUTO_FIELD allows custom definiation of primary key, e.g. Social 

#### `project/core/settings.py > INSTALLED_APPS`

`django.contrib.sessions`
lock you out for 5 mins for security purposes
keep the cart for 2 weeks

`django.contrib.staticfiles`
javascript, image, CSS

#### `project/manage.py`

* define basic py command
* allow customerize your command
* createsuperuser, not too many super user
* change_roles

## Starting An App

### Code

```bash
# create an app using 
python manage.py startapp APP

# run developmental server
python manage.py runserver
```

```py
# add INSTALLED_APPS to project/core/settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "NEW_APP",
]
```

## Create A Model

### Note

* update schema
* generate database migrations
* Do not make more than 5 modules for one app

1. Create a view on `app/views.py`
1. Add url pattern on `project/urls.py`
1. Add template on `app/templates/app/template.html`

### Code

```bash
#
python manage.py makemigrations

#
python manage.py migrate
```