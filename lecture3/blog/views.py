from django.shortcuts import render
<<<<<<< HEAD
import datetime
=======
from django import forms
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponseRedirect
>>>>>>> 2ac7a19cdec4f15dda4c1481ad219e48ede29057

# Create your views here.

a = []

class blogform(forms.Form):
    title = forms.CharField()
    property = forms.CharField()



def index(request):
<<<<<<< HEAD
    now = datetime.datetime.now()
    return render(request, "blog/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
=======
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
    
    
    
>>>>>>> 2ac7a19cdec4f15dda4c1481ad219e48ede29057
