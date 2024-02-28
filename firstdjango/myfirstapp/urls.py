from django.urls import path
from . import views

urlpatters = [
    # base url: /   views.function_name   name="name_of_function"
    path( "", views.home, name="home" )
]