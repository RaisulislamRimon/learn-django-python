from django.http import HttpResponse
from django.shortcuts import render
from .forms import LandingPageForm


def home_page(request, *args, **kwargs):
    print(request.method)
    title = "Welcome, home"
    form = LandingPageForm()
    # print(request.POST, request.GET)
    print(request.POST.get("email"))
    context = {"title": title, "form": form}
    return render(request, "home.html", context)


def about_page(request, *args, **kwargs):
    title = "Welcome, about"
    context = {"title": title}
    return render(request, "about.html", context)


# def home_page(*args, **kwargs):
#     return HttpResponse("<h1>Hello, Python & Django Home page</h1>")


# def base_page(request, *args, **kwargs):
#     return render(request, "base.html")


# def about_page(*args, **kwargs):
#     return HttpResponse("<h2>Python, Django about page</h2>")
