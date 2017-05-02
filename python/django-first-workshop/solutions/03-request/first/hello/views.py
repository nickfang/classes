from django.shortcuts import render
from django.http import HttpResponse


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
