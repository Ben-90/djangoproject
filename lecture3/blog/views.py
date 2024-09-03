from django.shortcuts import render
from django import forms
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponseRedirect


# Create your views here.

a = []

class blogform(forms.Form):
    title = forms.CharField()
    
    property = forms.CharField()



def index(request):

    return render(request, "blog/index.html", {
        "a": a,
    })
    
def add(request):
    if request.method == "POST":
        form = blogform(request.POST)
        if form.is_valid():
            
            title = form.cleaned_data["title"]
            property = form.cleaned_data["property"]
            a.append((title, property))
            return HttpResponseRedirect(reverse("blog:index"))
        else:
            return render(request, "blog/add.html", {
                "form": form
            })
    else:
        return render(request, "blog/add.html", {
            "form": blogform()
        })
    
    
    

