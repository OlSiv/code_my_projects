from django.http import HttpResponse
from django.shortcuts import render
from .models import Greeting


def index(request):
    return HttpResponse("Hello, world!")


def page2_view(request):
    return render(request, "page2.html")


def page3_view(request):
    all_greetings = Greeting.objects.all()
    return render(request, "page3.html", context={'data':all_greetings})

