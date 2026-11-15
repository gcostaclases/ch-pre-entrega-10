from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def inicio(request):
    return render(request, "posts/inicio.html")


def acerca(request):
    return render(request, "posts/acerca.html")


def lista_posts(request):
    # Me traigo los posts publicados y ordenados por fecha de creación descendente
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    # Creo el diccionario de contexto que voy a pasar al template
    context = {
        "posts": posts,
        "page_title": "Últimos posts",
    }
    return render(request, "posts/lista_posts.html", context)
