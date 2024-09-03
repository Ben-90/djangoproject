from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


class Newtasksform(forms.Form):
    tas = forms.CharField(label= "New Tasks")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(
        request, "tasks/index.html", {
            "tasks": request.session["tasks"]
        }
    )
    
def add(request):
    if request.method == "POST":
        form = Newtasksform(request.POST)
        if form.is_valid():
            tas = form.cleaned_data["tas"]
            request.session["tasks"] +=[tas]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render (request, 'tasks/add.html',{
                "form": form
            })
    return render(request, 'tasks/add.html', {
                "form": Newtasksform()
    })
