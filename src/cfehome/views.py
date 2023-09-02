from django.http import HttpResponse


def home_page(*args, **kwargs):
    return HttpResponse("<h1>Hello, Python & Django Home page</h1>")


def about_page(*args, **kwargs):
    return HttpResponse("<h2>Python, Django about page</h2>")
