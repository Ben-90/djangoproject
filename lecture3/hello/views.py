from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def brican(request):
    return HttpResponse("hello brican")

def ben(request):
    return HttpResponse("hello ben")

def gref(Request, name):
    return render(Request, "hello/greet.html", {
        "name": name.capitalize()
    })