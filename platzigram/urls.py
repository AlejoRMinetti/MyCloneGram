"""Platzigram URLs module."""

from django.urls import path
from django.http import HttpResponse


def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Hello, world!')

# visit http://127.0.0.1:8000/hello-world/
urlpatterns = [

    path('hello-world/', hello_world)

]
