from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def inicio(request):
    return render(request, "posts/inicio.html")


def acerca(request):
    return render(request, "posts/acerca.html")


def lista_posts(request):
    return render(request, "posts/lista_posts.html")
