
## Getting Started

**__init__.py**: a special file that tells python to treat this directory like a python package

**asgi.py** & **wsgi.py**: these are special configuration files that allow django to communicate with the web server. this does not require us to do anything.

**settings.py**: contains a bunch of settings and will be needed to install Django applications and plugins, change some middleware, and modify database engines.
 - Django is compatible with many different databases and can be configured within this settings file

**urls.py**: this will allow us to congifure different url routes that can route to different django applications

**manange.py**: acts a command line tool to run special commands related to database migrations, run the python server, and other things like creating users for the django admin panel

## Django Applications
the **firstdjango** directory is the django project which contains the files mentioned above. this is what is needed to execute code and make websites appear. The Django App is a standalone application that can be plugged and play with, meaning code in this django project can be put in another django project. these apps contains things like database models, different views or routes, templates, etc.

so we need to create an app. to do that, enter the following in the terminal:
```bash
cd firstdjango
#                         app name goes here
python3 manage.py startapp myfirstapp
```

the **myfirstapp** directory will contain a bunch of files we will need to work with.

to connect this with our django project with our app, go to the main folder, **firstdjango**, go to settings.py, and scroll down to `INSTALLED_APPS` and place a string containing the name of the new app.
```python
# Application definition
INSTALLED_APPS = [
    # "...",
    "myfirstapp"
]
```
adding this line essentially installs the application and allow our django project now view any code put in this app.

**about multiple apps**
different apps can be made for different purposes within a django app such as an app for authentication or specific user types (admins, moderators, etc.), apps to allow viewing the main content of the website. this is useful for separating different logic into its respective application.

now we'll go into the **myfirstapp** and create simple urls and routes. the files within this directory are as follows:
- **`__init__.py`**: see here for more information.
- **`admin.py`**: this allows us to register database models to view in our admin panel
- **`apps.py`**: we needn't worry about this one.
- **`models.py`**: this is where our database models will be placed and tested with automatic test cases.
- **`views.py`**: this is where mainly the work will be done and is where different views or routes will be created to access the website


## URL Configuration

while still in the **myfirstapp** directory we will create an additional file called **`urls.py`**. this will house different url routes to connect them to our views

we'll start by creating our first view and route to understand how things work. in **views.py**, we'll create a `home(request)` function where an object of request will be taken as a parameter which will allows us access to query parameters and body of different requests sent to this function. from here, a response will be returned (like a HTTP response or HTML template).

importing `HttpResonse`, we can return the message "Hello World" in the applications:
```py
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World!")
```

to receive this resposne, it needs to be connected to the applicatino through a route or a url. in the **urls.py** file we created, we'll need to set it up as such:

paths are defined in this format:
```py
from django.urls import path
from . import views

urlpatters = [
    # base url: /   views.function_name   name="name_of_function"
    path( "", views.home, name="home" )
]
```
so when accessing this path of an empty string, it will access a function in the views.py and return the response that will be viewed

now to connect this url to our application, go bac to the **firstdjango** directory, and access to its **urls.py** file. here we'll make a url route that connects to our app. in this type of file, routes to our specific apps will be declared here to be able to access them. this link will be created by doing the following:
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ! add this line:
    path( "", include("myfirstapp.urls") )
]
```

this will access the app's **urls.py** file and then access that declared string. so after the domain's name, the string that its detecting has its own functionality in its app's **urls.py** file.

for example, if this line was written like this in `firstdjango/urls.py`:
```py
path( "myapp/", include("myfirstapp.urls") )
```

after the domain name, 'myapp/' needs to be added (http://www.domain.com/**myapp/home**). then it will connect to the `myfirstapp/urls.py` file to access the rest of that route:
```py
urlpatters = [
    # base url: /   views.function_name   name="name_of_function"
    path( "home", views.home, name="home" )
]
```
so the main part of the route is accessed in the **firstdjango** directory whereas the more particualr logic of the route afterwards is handled in the **myfirstapp** directory.

this is great because that means different prefixes can be made for different applications with similar urls that are within them but can still be accessed with the declared prefix.

## running the server

run the server with this command:
```bash
python3 manage.py runserver
```