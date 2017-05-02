from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def hello(request):
    return HttpResponse(u"नमस्कारम एव्रीबडियम")


def named(request, name):
    return HttpResponse(u"नमस्कारम " + name)


def path(request):
    return HttpResponse(request.path)


def query(request):
    return HttpResponse(repr(request.GET), content_type="text/plain")


def method(request):
    return HttpResponse(request.method)


def headers(request):
    return HttpResponse(repr(request.META), content_type="text/plain")


def index(request):
    return render(
        request, "index.html", {"request": request, "now": datetime.now()}
    )


def about(request):
    return render(request, "about.html")


def support(request):
    return render(request, "support.html")
