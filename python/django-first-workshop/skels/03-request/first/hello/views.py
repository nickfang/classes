from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse(u"नमस्कारम एव्रीबडियम")


def named(request, name):
    return HttpResponse(u"नमस्कारम " + name)

# TODO: view for full path
# TODO: view for query params
# TODO: view for method name
# TODO: view for headers
