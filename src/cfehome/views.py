from django.http import HttpResponse
from django.shortcuts import render


# def home_page(*args, **kwargs):
#     return HttpResponse("<h1>Hello, Python & Django Home page</h1>")


def home_page(request, *args, **kwargs):
    return render(request, "index.html")


def about_page(*args, **kwargs):
    return HttpResponse("<h2>Python, Django about page</h2>")
