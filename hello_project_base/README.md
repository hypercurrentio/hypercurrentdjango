# Getting Started
Steps to integrate Revenium Middleware with any Django Application


## Project Setup

Open project in desired editor. All commands should be done through the command line

### Ensure Django is installed 

```shell
pip install Django==desired_version
```


### Create a Virtual Environment

```shell
python -m venv venv
source venv/bin.activate
```

### Install Dependencies

```shell
pip install django djangorestframework
```
### Create New Django Project

```shell
django-admin startproject project_name
cd project_name
```

### Create new Django Application

```shell
python manage.py startapp app_name
```

## Application Setup 

Basic starter app with Revenium Middleware

### Add apps to INSTALLED_APPS which is part of the settings.py file inside of the base project

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'hello_app',
]
```

### Setup a Simple View Inside of your app 

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})
```

### Add urls.py to your app

```python
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
]
```
### Link your app to your project in the urls.py file inside of the proct

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hello_app.urls')),
]
```

## Go To the README at this base of this repository to see how to integrate the middleware.
See hello_project_base/hello_project_base/settings.py to see example of a project with the Revenoum Middleware integrated


