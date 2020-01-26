from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):
    context = {
        "message": "Hello World"
    }
    return render(request, 'index.html', context)
