from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "index"),
    path("<str:name>", views.gref, name = "name"),
    path("brican", views.brican, name = "bric"),
    path("about", views.ben, name = "about"),
]
