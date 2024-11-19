# S01N02 Django Introduction

## module

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

## terminal, bash, CMD (command prompt)

> mkdir
> virtualenv venv
> source venv/bin/activate
> pip install django
> pip install pillow (for python images)
> pip freeze (list all library installed in the activated virtual env)
> pip freeze > requirements.txt
> django-admin
> django-admin startproject

step
install virtual environment once per new project
close the door to the framework, django
activate virtualenv
have same version of library when git or sharing e.g. 5.1.3
download Python extensions on virutal studio code
django-admin is modular, many apps under one project
myfirstproject/myfirstproject > core > settings

new computer, new virutal environment

## __init__.py in the core is usually empty

create module with __init__
parse different parts of url 
request from asgi.py or wsgi.py are redirected to urls.py
asgi and wsgi are entry points

## settings.py

SECRET_KEY is stored at global environment
DEBUG should be changed to False in production
ALLOWED_HOSTS lists domain name or ip address
INSTALLED_APPS manages 
MIDDLEWARE manages requests
TEMPLATES is html page
TEMPLATES[0]["DIRS"] global page like entry
TEMPLATES[0]["DIRS"] specific page like admin?
DATABASES has built-in sqlite3, usually progresql
DATABASES, unless old databases
AUTH_PASSWORD_VALIDATORS, have cap letter
STATIC_URL is usually changed in production mode
DEFAULT_AUTO_FIELD allows custom definiation of primary key, e.g. Social 

django.contrib.sessions
lock you out for 5 mins for security purposes
keep the cart for 2 weeks

django.contrib.staticfiles
javascript, image, CSS

manage.py define basic py command
customerize your command
createsuperuser, not too many super user
change_roles

## create database to store users

> python manage.py migrate, create database on app pre-installed 
> python manage.py createsuperuser
> python manage.py makemigration

run developmental server
python manage.py runserver
python manage.py startapp blog

add INSTALLED_APPS to settings

MVC
model > model
template > view to be created
views > controller

update schema
generate database migrations

## Model

not to have more than 5 modules for one app
> python manage.py makemigrations
> python manage.py migrate