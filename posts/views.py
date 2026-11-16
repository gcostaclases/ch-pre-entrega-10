from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def inicio(request):
    return render(request, "posts/inicio.html")


def acerca(request):
    return render(request, "posts/acerca.html")


# ---- READ POSTS ----
def lista_posts(request):
    # Me traigo los posts publicados y ordenados por fecha de creación descendente
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    # Creo el diccionario de contexto que voy a pasar al template
    context = {
        "posts": posts,
        "page_title": "Últimos posts",
    }
    return render(request, "posts/lista_posts.html", context)


def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, "posts/detalle_post.html", {
        "post": post
    })


# ---- CREATE POST ----
def crear_post(request):
    # Si el usuario envió el formulario
    if request.method == "POST":

        # Creamos un formulario con los datos enviados por el usuario y los archivos subidos (si los hay)
        form = PostForm(request.POST, request.FILES)

        # Le pedimos a Django que valide el formulario y si es válido, que nos devuelva los datos limpios
        if form.is_valid():
            # Como estamos usando ModelForm, Django sabe cómo crear un objeto Post y guardarlo en la base de datos.
            form.save()
            # Redirige a la lista de posts después de crear uno nuevo
            return redirect("lista_posts")
    # Si no es un método POST, si es solo ver el formulario para crear un nuevo post
    else:
        form = PostForm()

    # Si está vacío que renderice el formulario para crear un nuevo post
    return render(request, "posts/post_form.html", {
        "form": form,
        "page_title": "Crear nuevo post",
        "texto_boton": "Crear post"
    })


# ---- UPDATE POST ----
def editar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect("detalle_post", slug=post.slug)

    else:
        form = PostForm(instance=post)

    return render(request, "posts/post_form.html", {
        "form": form,
        "post": post,
        "page_title": "Editar post",
        "texto_boton": "Guardar cambios"
    })


# ---- DELETE POST ----
def eliminar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect("lista_posts")

    return render(request, "posts/post_confirm_delete.html", {
        "post": post
    })
